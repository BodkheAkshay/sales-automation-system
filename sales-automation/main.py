from data_generator import insert_daily_sales
from sales_analyzer import run_agent

# Step 1: Insert daily data
insert_daily_sales()

# Step 2: Run monitoring agent
run_agent()


print("\nPipeline execution finished successfully.")
