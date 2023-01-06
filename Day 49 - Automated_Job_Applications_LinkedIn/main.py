# Automated bot to send applies to all job applications for specific job position on LinkedIn
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from dotenv import load_dotenv
load_dotenv()

LINKEDIN_URL = os.getenv('LINKEDIN_JOB_SEARCH_URL')  # this url is for "python developer" jobs
LINKEDIN_ACCOUNT_EMAIL = os.getenv('LINKEDIN_ACCOUNT_EMAIL')
LINKEDIN_ACCOUNT_PASSWORD = os.getenv('LINKEDIN_ACCOUNT_PASSWORD')
PHONE = os.getenv('TEL')

chromedriver_path ="C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get(LINKEDIN_URL)

# Sign In
sign_in_btn = driver.find_element_by_link_text("Sign in")
sign_in_btn.click()
sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys(LINKEDIN_ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(LINKEDIN_ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

sleep(5)

all_applications = driver.find_elements_by_css_selector(".job-card-container--clickable")

for application in all_applications:
    print("Called")
    application.click()
    sleep(2)
    
    try:        
        apply_btn = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_btn.click()
        sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)
        # Submit application
        submit_btn = driver.find_element_by_css_selector("footer button")

        if submit_btn.get_attribute("data-control-name") == "continue_unify":
            close_btn = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_btn.click()
            sleep(2)
            discard_btn = driver.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_btn.click()
            print("Complex application. [Skipped]")
            continue
        else:
            submit_btn.click()
        
        sleep(2)
        close_btn = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_btn.click()
    except NoSuchElementException:
        print("No application button found [Skipped]")
        continue

sleep(5)
driver.quit()