import csv
import time
import wget
import xlsxwriter
import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from termcolor import colored
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import random



excel_file_path = 'users(unfollow).xlsx'  # Replace with the actual path to your Excel file

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')
# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)
#users to unfollow
users = df.iloc[:, 0].tolist()
username = input("Username:")
password = input("Password:")
maxLimit = input("Maximum number of users you want to unfollow in an hour ")
minLimit = input("Minimum number of users you want to unfollow in an hour ")
#Specify gap between unfollowing (If wanting to unfollow <20 and >1 in a min set a = 60/20 and b= 60)
a = int(3600/int(maxLimit))
b = int(3600/int(minLimit))

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
profile_name = ['koustubh']
time.sleep(random.uniform(3, 4))

# Click on home page
user_profile_icon = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                     "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")))
user_profile_icon.click()

# Handle "Not Now" button
try:
    not_now_2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Not Now"]')))
    not_now_2.click()
except:
    pass
# Maximizing Window
browser.maximize_window()

for user in users:
    #searching user
    time.sleep(random.randrange(12, 18))
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href= '#']"))).click()
    time.sleep(5)
    #Entering Name
    s = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@aria-label, 'Search input')]"))).send_keys(
        user)
    time.sleep(5)

    try:
        #Entering and unfollowing user
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/"+user[1:]+"/')]"))).click()
        time.sleep(3)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, '_acan')]"))).click()
        time.sleep(3)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//span[text()='Unfollow']"))).click()
        time.sleep(random.randrange(a, b))
    except:
        #IF wrong username
        print("Wrong username:", user)

time.sleep(3)
browser.quit()