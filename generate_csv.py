import pandas as pd
import random
from datetime import datetime, timedelta

# Generate 50 random customer IDs
customer_ids = [i for i in range(101, 151)]

# Vehicle data
vehicles = ["SUV X", "SUV Y", "Sedan A", "Sedan B"]
categories = ["Automobile", "Automobile", "Automobile", "Automobile"]
regions = ["Region A", "Region B", "Region C"]
segments = ["Young Families", "Urban Professionals", "Retirees"]

# Generate sales data (sales_data.csv)
sales_data = []
for _ in range(50):
    customer = random.choice(customer_ids)
    vehicle_idx = random.randint(0, 3)
    sale_date = datetime.today() - timedelta(days=random.randint(0, 90))
    region = random.choice(regions)
    sales_amount = random.randint(25000, 50000)

    sales_data.append([customer, vehicles[vehicle_idx], categories[vehicle_idx], sale_date.strftime("%Y-%m-%d"), region,
                       sales_amount])

sales_df = pd.DataFrame(sales_data,
                        columns=["customer_id", "product", "category", "sale_date", "region", "sales_amount"])

# Generate campaign outcomes (campaign_outcomes.csv)
campaign_names = ["SUV Promo Q1", "Sedan Offer", "Winter SUV Sale", "Spring Sedan Discount"]
campaign_data = []
for i in range(50):
    campaign_id = f"{i + 1:03}"
    campaign_name = random.choice(campaign_names)
    start_date = datetime.today() - timedelta(days=random.randint(30, 90))
    end_date = start_date + timedelta(days=random.randint(15, 30))
    target_segment = random.choice(segments)
    click_rate = f"{random.randint(10, 20)}%"
    conversion_rate = f"{random.randint(3, 8)}%"
    sales_generated = random.randint(50, 150)

    campaign_data.append(
        [campaign_id, campaign_name, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"), target_segment,
         click_rate, conversion_rate, sales_generated])

campaign_df = pd.DataFrame(campaign_data,
                           columns=["campaign_id", "campaign_name", "start_date", "end_date", "target_segment",
                                    "click_rate", "conversion_rate", "sales_generated"])

# Generate audience segments (audience_segments.csv)
audience_data = []
for i in range(50):
    segment_id = f"A{i + 1}"
    segment_name = random.choice(segments)
    age_range = f"{random.randint(25, 50)}-{random.randint(40, 65)}"
    income_level = f"{random.randint(40, 100)}k-{random.randint(70, 150)}k"
    preferred_vehicle = random.choice(vehicles)
    past_purchases = random.choice(vehicles)

    audience_data.append([segment_id, segment_name, age_range, income_level, preferred_vehicle, past_purchases])

audience_df = pd.DataFrame(audience_data,
                           columns=["segment_id", "segment_name", "age_range", "income_level", "preferred_vehicle",
                                    "past_purchases"])

# Save CSV files
sales_df.to_csv("sales_data.csv", index=False)
campaign_df.to_csv("campaign_outcomes.csv", index=False)
audience_df.to_csv("audience_segments.csv", index=False)

# Return sample data preview
sales_df.head(), campaign_df.head(), audience_df.head()
