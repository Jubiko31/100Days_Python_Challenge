# Amazon product price tracker
# When specific product price is less than particular amount Python bot sends you notification on email
import os
import lxml
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

SMTP_ADDRESS = os.getenv('SMTP_ADDRESS')
EMAIL = os.getenv('CRED_EMAIL')
PASSWORD = os.getenv('CRED_PASSWORD')
PRODUCT_URL = os.getenv('PRODUCT_URL')
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=PRODUCT_URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price_curr = soup.find(id="priceblock_ourprice").get_text()
price = float(price_curr.split('$')[1])

# Send Email when price is under $100
title = soup.find(id="productTitle").get_text().strip()

if price < 100: # or any specific amount
    msg = f"{title} is now {price_curr}"
    
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as conn:
        conn.starttls()
        res = conn.login(EMAIL, PASSWORD)
        conn.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{msg}\n{PRODUCT_URL}"
        )