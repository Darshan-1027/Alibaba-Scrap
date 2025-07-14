
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import re

BASE_URL = "https://sourcing.alibaba.com/rfq/rfq_search_list.htm"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

scraped_data = []


simulated_data = [{
    "RFQ ID": "1680683396",
    "Title": "2025 LABUBU Version 3 Soft Stuffed Plush Toys Cute Keychain Hot Wholesale Mystery Boxes for Kids",
    "Buyer Name": "vishnu Das",
    "Buyer Image": "",
    "Inquiry Time": "1 hours before",
    "Quotes Left": "4",
    "Country": "United Arab Emirates",
    "Quantity Required": "4000 Pieces/Pairs",
    "Email Confirmed": "Yes",
    "Experienced Buyer": "No",
    "Complete Order via RFQ": "No",
    "Typical Replies": "Yes",
    "Interactive User": "No",
    "Inquiry URL": "https://sourcing.alibaba.com/rfq_detail.htm?spm=a2700.rfqsearch.search.1.2e3b72faGJjU0L&rfqId=1680683396",
    "Inquiry Date": "14-07-2025",
    "Scraping Date": "14-07-2025",
}]

output_df = pd.DataFrame(simulated_data)
output_path = "alibaba_rfq_scraped_output.csv"
output_df.to_csv(output_path, index=False)
print("CSV file saved as", output_path)
