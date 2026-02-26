import pymysql
import pandas as pd
from alert import send_email_alert


def run_agent():

    # CONNECT TO MYSQL
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Mysql_pass",    # Add your MySQL password here
        database="ecommerce_agent",
        port=3306
    )


    # LOAD SALES DATA

    query = "SELECT * FROM sales"
    df = pd.read_sql(query, conn)

    # Ensure correct date format
    df['order_date'] = pd.to_datetime(df['order_date'])


    # DATA CLEANING
    
    df['sales_amount'] = df['sales_amount'].fillna(0)
    df['return_amount'] = df['return_amount'].fillna(0)
    df['region'] = df['region'].fillna("Unknown")
    df['product_name'] = df['product_name'].fillna("Unknown")


    # CHECK DATA AVAILABILITY
    
    if df.empty:
        send_email_alert(
            "No sales data available in database.",
            "Check data ingestion pipeline."
        )
        conn.close()
        return


    # Yesterday vs Day-Before-Yesterday

    yesterday_date = df['order_date'].max()
    day_before_yesterday = df[df['order_date'] < yesterday_date]['order_date'].max()

    if pd.isna(day_before_yesterday):
        send_email_alert(
            "Insufficient historical data.",
            "Cannot compare yesterday with previous day."
        )
        conn.close()
        return

    yesterday_df = df[df['order_date'] == yesterday_date]
    day_before_df = df[df['order_date'] == day_before_yesterday]

    
    # REVENUE COMPARISON

    yesterday_sales = yesterday_df['sales_amount'].sum()
    day_before_sales = day_before_df['sales_amount'].sum()

    if day_before_sales == 0:
        send_email_alert(
            "Previous day sales is zero.",
            "Cannot calculate drop percentage."
        )
        conn.close()
        return

    drop_percent = ((day_before_sales - yesterday_sales) / day_before_sales) * 100

    print("\n===== SALES SUMMARY =====")
    print("Yesterday Date:", yesterday_date.date())
    print("Day Before Yesterday:", day_before_yesterday.date())
    print("Yesterday Sales:", yesterday_sales)
    print("Day Before Sales:", day_before_sales)
    print("Drop %:", round(drop_percent, 2))



    # REGION PERFORMANCE
   
    region_yesterday = yesterday_df.groupby('region')['sales_amount'].sum()
    region_day_before = day_before_df.groupby('region')['sales_amount'].sum()

    region_change = region_yesterday.subtract(region_day_before, fill_value=0)
    worst_region = region_change.idxmin()


    # PRODUCT DECLINE

    product_yesterday = yesterday_df.groupby('product_name')['sales_amount'].sum()
    product_day_before = day_before_df.groupby('product_name')['sales_amount'].sum()

    product_change = product_yesterday.subtract(product_day_before, fill_value=0)
    declining_product = product_change.idxmin()


    # RETURN SPIKE
    return_yesterday = yesterday_df['return_amount'].sum()
    return_day_before = day_before_df['return_amount'].sum()


    # GENERATE BUSINESS INSIGHT
    insight = f"""
Sales dropped by {round(drop_percent,2)}%.
Worst performing region: {worst_region}.
Declining product: {declining_product}.
"""

    if return_yesterday > return_day_before:
        insight += " Return spike detected."

    print("\n===== BUSINESS INSIGHT =====")
    print(insight)

    # AGENT SUGGESTED ACTION
    suggestion = ""

    if drop_percent > 20:
        suggestion += "Run marketing campaign. "

    if return_yesterday > return_day_before:
        suggestion += "Check product quality & return reasons. "

    suggestion += f"Focus on improving sales in {worst_region} region."

    print("\n===== SUGGESTED ACTION =====")
    print(suggestion)

   
    # EMAIL TRIGGER CONDITION
    if drop_percent > 15 or return_yesterday > return_day_before:
        print("\nTriggering email alert...")
        send_email_alert(insight, suggestion)
    else:
        print("\nNo major issue detected. Email not sent.")

    
    # CLOSE CONNECTION

    conn.close()
    print("\nAgent run completed.")


if __name__ == "__main__":
    run_agent()