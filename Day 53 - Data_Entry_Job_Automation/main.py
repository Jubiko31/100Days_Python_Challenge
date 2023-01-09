# Program auto fills google form and creates google sheet data (address, price, link) from filtered url of Georgia's biggest real estate platform.
# You can view in-action in Gallery
import os
import requests
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

GOOGLE_FORMS_URL = os.getenv('GOOGLE_FORMS_URL')
MYHOME_FILTERED_URL= os.getenv('MYHOME_FILTERED_URL')
chromedriver_path ="C:\Development\chromedriver.exe"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ka;q=0.7,ru;q=0.6"
}

response = requests.get(MYHOME_FILTERED_URL, headers=header)
data = response.text

soup = BeautifulSoup(data, "html.parser")

all_houses = soup.select(".statement-card a")
all_urls = []

for house in all_houses:
    href = house["href"]
    all_urls.append(href)

addresses_txt = soup.select(".address")
addresses = [address.get_text() for address in addresses_txt]

prices_txt = soup.select(".item-price-gel")
prices = [price.get_text() for price in prices_txt]
        
# Create a Spreadsheet using Google Form
driver = webdriver.Chrome(executable_path=chromedriver_path)

for idx in range(len(all_urls)):
    driver.get(GOOGLE_FORMS_URL)
    sleep(2)
    address = driver.find_element("xpath",
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element("xpath",
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element("xpath",
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    
    address.send_keys(addresses[idx])
    price.send_keys(prices[idx])
    link.send_keys(all_urls[idx])
    submit.click()