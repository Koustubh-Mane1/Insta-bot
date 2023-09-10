import csv
import time
import sys
import wget
import xlsxwriter
import openpyxl
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import random


excel_file_path = 'users(like).xlsx'  # Replace with the actual path to your Excel file

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)
df = df.drop_duplicates()


users = df.iloc[:, 0].tolist()
username = input("Username:")
password = input("Password:")
maxLimit = input("Maximum number of posts you have to like in an hour")
browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')

try:
    # Accept cookies
    accept_cookies = browser.find_element(By.XPATH, '//button[text()="Accept"]')
    accept_cookies.click()
except:
    pass


def auth(username, password):
    try:
        browser.get('https://instagram.com')
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        # Entering username, password
        input_username = browser.find_element(By.NAME, 'username')
        input_password = browser.find_element(By.NAME, 'password')

        input_username.send_keys(username)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        input_password.send_keys(password)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
        )
        # Logging in
        input_password.send_keys(Keys.ENTER)

        # Wait for login
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]'))
        )
    except Exception as err:
        print("Did not log in")
        browser.quit()


auth(username, password)

# Cookies
try:
    not_now_1 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Not Now"]'))
    )
    not_now_1.click()
except:
    pass

# Notifications
try:
    not_now_2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Not Now"]'))
    )
    not_now_2.click()
except:
    pass

# Input after Login
time.sleep(random.uniform(3, 4))

# Click the user's profile icon
user_profile_icon = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")))
user_profile_icon.click()

# Handle "Not Now" button
try:
    not_now_2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Not Now"]')))
    not_now_2.click()
except:
    pass

browser.maximize_window()
for user in users:
    time.sleep(5)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href= '#']"))).click()
    time.sleep(5)

    s = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@aria-label, 'Search input')]"))).send_keys(user)
    time.sleep(5)

    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/"+user[1:]+"/')]"))).click()
        time.sleep(3)
        browser.find_element(By.XPATH, '//div[@class="_aagu"]').click()
        time.sleep(5)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='_aamw']"))).click()
        time.sleep(1)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class ='x160vmok x10l6tqk x1eu8d0j x1vjfegm']"))).click()
        print("Liked ", user)
        time.sleep(5)
        blacklist.append(user)

    except:
        user_profile_icon = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                             "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")))
        user_profile_icon.click()

        print("Wrong username:",user)

# Step 4: Save the DataFrame to an Excel file
df.to_excel('Blacklist.xlsx', index=False)
time.sleep(3)
browser.quit()