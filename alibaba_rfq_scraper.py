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

# Alibaba site uses JS, so normally selenium is needed. Here we assume a simplified static simulation
for page in range(1, 3):  # Test with first 2 pages. You can expand to all
    params = {
        "country": "AE",
        "recently": "Y",
        "page": page
    }
    res = requests.get(BASE_URL, headers=HEADERS, params=params)
    soup = BeautifulSoup(res.text, "html.parser")

    listings = soup.find_all("div", class_=re.compile("card-rfq-item"))
    for item in listings:
        title = item.find("a", class_="title")
        title_text = title.text.strip() if title else ""
        inquiry_url = "https:" + title["href"] if title else ""
        
        details = item.text.strip()

        # Extract individual details using regex or search techniques
        buyer_name = item.find("div", class_="user-name")
        buyer = buyer_name.text.strip() if buyer_name else ""

        country_img = item.find("img", class_="country-flag")
        country = country_img["alt"] if country_img else ""

        quantity_match = re.search(r"Quantity Required:\s+(\d+.*?)\s", details)
        quantity = quantity_match.group(1) if quantity_match else ""

        quotes_match = re.search(r"Quotes Left\s+(\d+)", details)
        quotes = quotes_match.group(1) if quotes_match else ""

        time_match = re.search(r"Date Posted:\s+(.+?)\s", details)
        inquiry_time = time_match.group(1) if time_match else ""

        today = datetime.today().strftime("%d-%m-%Y")

        scraped_data.append({
            "RFQ ID": "",  # Not available in list, needs detail page
            "Title": title_text,
            "Buyer Name": buyer,
            "Buyer Image": "",
            "Inquiry Time": inquiry_time,
            "Quotes Left": quotes,
            "Country": country,
            "Quantity Required": quantity,
            "Email Confirmed": "",
            "Experienced Buyer": "",
            "Complete Order via RFQ": "",
            "Typical Replies": "",
            "Interactive User": "",
            "Inquiry URL": inquiry_url,
            "Inquiry Date": today,
            "Scraping Date": today,
        })

    time.sleep(2)


output_df = pd.DataFrame(scraped_data)
output_df.to_csv("Scrap.csv",index=Fasle)
