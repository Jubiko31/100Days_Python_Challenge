# Automated Tinder swiper bot
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from dotenv import load_dotenv
load_dotenv()

FACEBOOK_EMAIL = os.getenv('FB_EMAIL')
FACEBOOK_PASSWORD = os.getenv('FB_PASSWORD')

chromedriver_path ="C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("https://tinder.com")

sleep(2)
login_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_btn.click()

sleep(2)
fb_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)
main_window = driver.window_handles[0]
fb_login_page = driver.window_handles[1]
driver.switch_to.window(fb_login_page)
# Login to FB
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(FACEBOOK_EMAIL)
password.send_keys(FACEBOOK_PASSWORD)
password.send_keys(Keys.ENTER)
driver.switch_to.window(main_window)
# Allow Loaction, Notifications and Cookies
sleep(5)
allow_location = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
notifications = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications.click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for _ in range(100):   # 100 like attempts for free account per day
    sleep(1)
    try:
        print("called")
        like = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)
driver.quit()