import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_sales_data(num_records=50):
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(num_records)]
    regions = ['North', 'South', 'East', 'West']
    products = ['SUV', 'Sedan', 'Hatchback', 'Truck', 'Minivan']
    sales = np.random.randint(50, 300, num_records)
    data = {'Date': dates, 'Region': np.random.choice(regions, num_records), 'Product': np.random.choice(products, num_records), 'Sales': sales}
    return pd.DataFrame(data)

def generate_campaigns_data(num_records=50):
    campaign_ids = [f"Campaign{i+1}" for i in range(num_records)]
    regions = ['North', 'South', 'East', 'West']
    products = ['SUV', 'Sedan', 'Hatchback', 'Truck', 'Minivan']
    outcomes = ['Positive', 'Negative', 'Neutral', 'Very Positive', 'Very Negative']
    data = {'CampaignID': campaign_ids, 'Region': np.random.choice(regions, num_records), 'Product': np.random.choice(products, num_records), 'Outcome': np.random.choice(outcomes, num_records)}
    return pd.DataFrame(data)

def generate_segments_data(num_records=50):
    customer_ids = range(1, num_records + 1)
    ages = np.random.randint(18, 65, num_records)
    incomes = np.random.randint(30000, 100000, num_records)
    interests = [", ".join(random.sample(['Tech', 'Travel', 'Family', 'Home', 'Music', 'Gaming', 'Luxury', 'Dining', 'Gardening', 'DIY', 'Fitness', 'Outdoors', 'Art', 'Culture', 'Sports','Finance'], k=random.randint(2, 4))) for _ in range(num_records)]
    segments = np.random.choice(['Urban Professionals', 'Suburban Families', 'Young Adults', 'Affluent Individuals', 'Home Owners', 'Active Lifestyles', 'Creative Enthusiasts', 'Senior Professionals', 'Gen Z', 'Foodies','Tech Savvy', 'Entertainment Seekers','Music Lovers','Home Makers','Sports Fans','Financial Experts'], num_records)
    data = {'CustomerID': customer_ids, 'Age': ages, 'Income': incomes, 'Interests': interests, 'Segment': segments}
    return pd.DataFrame(data)

sales_df = generate_sales_data()
campaigns_df = generate_campaigns_data()
segments_df = generate_segments_data()

sales_df.to_csv('sales.csv', index=False)
campaigns_df.to_csv('campaigns.csv', index=False)
segments_df.to_csv('segments.csv', index=False)

print("sales.csv, campaigns.csv, and segments.csv files generated.")