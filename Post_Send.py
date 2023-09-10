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

excel_file_path = 'users(recentpost).xlsx'  # Replace with the actual path to your Excel file

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)
#users to unfollow
users = df.iloc[:, 0].tolist()
username = input("Username:")
password = input("Password:")


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

def send_message(users, messages):
    try:
        #Notnow1
        not_now_buttons = browser.find_elements(By.XPATH, '//button[text()="Not Now"]')
        for button in not_now_buttons:
            button.click()
            time.sleep(random.uniform(1, 3))        #Notnow2
        time.sleep(random.randrange(3,5))
        time.sleep(5)
        #Profile button
        browser.find_element(By.XPATH,'//div[@class="x1n2onr6"]').click()
        time.sleep(random.randrange(3,4))
        time.sleep(5)

        #Selecting most recent post
        browser.find_element(By.XPATH,'//div[@class="_aagu"]').click()
        time.sleep(random.randrange(3,4))
        time.sleep(5)

        #Share button
        browser.find_element(By.XPATH,'//div[@class="_abm0 _abl_"]').click()
        time.sleep(random.randrange(3,4))
        time.sleep(5)

        #Entering user names
        for user in users:
            browser.find_element(By.NAME,'queryBox').send_keys(user)
            time.sleep(random.randrange(8,10))
            browser.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z xdt5ytf x2lah0s x193iq5w xeuugli xamitd3 x78zum5"]').click()
            time.sleep(random.randrange(3,4))
            print(f'Post selected for {user}')
        #Entering message in messaging area
        text_area = browser.find_element(By.NAME,'shareCommentText')
        text_area.send_keys(messages)
        time.sleep(random.randrange(3,5))
        #Sending post 
        browser.find_element(By.XPATH,'//div[@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x9bdzbf x1ypdohk x1i0vuye x1f6kntn xwhw2v2 x10w6t97 xl56j7k x17ydfre x1swvt13 x1pi30zi x1n2onr6 x2b8uid xlyipyv x87ps6o xcdnw81 xh8yej3 x1tu34mt xzloghq x3nfvp2"]').click()
        time.sleep(random.randrange(3,4))
        
    except Exception as err:
        print(err)
    browser.quit()



#Info
auth(username, password)
time.sleep(random.randrange(2,4))
send_message(users, message)
