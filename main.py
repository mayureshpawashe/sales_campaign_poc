import pandas as pd

# Load CSV files
sales_df = pd.read_csv("data1/sales_data.csv")
campaign_df = pd.read_csv("data1/campaign_outcomes.csv")
audience_df = pd.read_csv("data1/audience_segments.csv")

# Preview data
print(sales_df.head(), campaign_df.head(), audience_df.head())
