# Automative python bot for "Cookie Clicker" game:
# Original: https://orteil.dashnet.org/cookieclicker/
from selenium import webdriver
from time import time

chromedriver_path ="C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time() + 5
limit = time() + 60 * 5 # 5 min

while True:
    cookie.click()
    if time() > timeout:
        prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []
        for price in prices:
            txt = price.text
            if txt != "":
                cost = int(txt.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        # Cookie upgrading
        upgrades = {}
        for idx in range(len(item_prices)):
            upgrades[item_prices[idx]] = item_ids[idx]
        money = driver.find_element_by_id("money").text
        if "," in money:
            money = money.replace(",", "")
        count = int(money)
        # Buy upgrades
        affordable_upgrades = {}
        for cost, idx in upgrades.items():
            if count > cost:
                affordable_upgrades[cost] = idx
        most_expensive = max(affordable_upgrades)
        purchase_id = affordable_upgrades[most_expensive]
        driver.find_element_by_id(purchase_id).click()
        
        timeout = time() + 5
    
    if time() > limit:
        cps = driver.find_element_by_id("cps").text  # Cookies per second
        print(cps)
        break
