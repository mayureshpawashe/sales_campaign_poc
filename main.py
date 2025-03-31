import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
import os

load_dotenv()

# Load CSV data
sales_data = pd.read_csv("data/sales.csv")
campaign_data = pd.read_csv("data/campaigns.csv")
segment_data = pd.read_csv("data/segments.csv")
