import pymysql
from faker import Faker
import random
from datetime import date, timedelta

fake = Faker()

def insert_daily_sales():

    print("Generating daily sales data...")

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="##########",    # Add your MySQL password here 
        database="ecommerce_agent",
        port=3306
    )

    cursor = conn.cursor()

    # Generate for Yesterday
    sales_date = date.today() - timedelta(days=1)

    regions = ["North", "South", "East", "West"]

    cities_by_region = {
        "North": ["Delhi", "Lucknow"],
        "South": ["Bangalore", "Hyderabad"],
        "West": ["Mumbai", "Pune"],
        "East": ["Kolkata", "Patna"]
    }

    categories = ["Electronics", "Clothing", "Home", "Beauty"]

    products = {
        "Electronics": ["Wireless Earbuds", "Smart Watch"],
        "Clothing": ["Men T-Shirt", "Women Kurti"],
        "Home": ["Mixer Grinder", "Cookware Set"],
        "Beauty": ["Face Cream", "Perfume"]
    }

    channels = ["App", "Website", "Amazon", "Flipkart", "Retail Store", "Instagram"]

    data = []

    for i in range(20):

        region = random.choice(regions)
        city = random.choice(cities_by_region[region])
        category = random.choice(categories)
        product = random.choice(products[category])

        sales_amount = random.randint(800, 18000)
        orders_count = random.randint(1, 40)
        discount_amount = random.randint(100, 2000)
        return_amount = random.randint(0, 800)
        channel = random.choice(channels)

        data.append((
            sales_date,
            region,
            city,
            category,
            product,
            sales_amount,
            orders_count,
            discount_amount,
            return_amount,
            channel
        ))

    query = """
    INSERT INTO sales
    (order_date, region, city, category, product_name,
     sales_amount, orders_count, discount_amount, return_amount, channel)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.executemany(query, data)
    conn.commit() 

    print(f"Sales records inserted successfully for {sales_date}!")

    conn.close()


if __name__ == "__main__":
    insert_daily_sales()