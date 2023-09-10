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


excel_file_path = 'users(dm).xlsx'  # Replace with the actual path to your Excel file
blacklist_file = 'blacklist.xlsx'  # Replace with the actual path to your Excel file

# Read the Excel file into a pandas DataFrame

df = pd.read_excel(excel_file_path)
bl_df = pd.read_excel(blacklist_file)
df = df.drop_duplicates()
blacklist = bl_df.iloc[:, 0].tolist()
df = df[~df['Username'].isin(blacklist)]
#users to unfollow
users = df.iloc[:, 0].tolist()
username = input("Username:")
password = input("Password:")

messages = df.iloc[:, 1].tolist()
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
    except Exception as err:
        print("Did not log in")
        browser.quit()


auth(username, password)


# Cookies
try:
    not_now_1=browser.find_element_by_xpath('//button[text()="Not Now"]')
    not_now_1.click()
    time.sleep(2)
except:
    pass

# Notifications
try:
    not_now_2=browser.find_element_by_xpath('//button[text()="Not Now"]')
    not_now_2.click()
    time.sleep(2)
except:
    pass

# Input after Login
time.sleep(7)
browser.find_element(By.XPATH,"//a[contains(@href, '/?next=')]").click()
time.sleep(random.randrange(3,4))
try:
    not_now_2=browser.find_element_by_xpath('//button[text()="Not Now"]')
    not_now_2.click()
    time.sleep(2)
except:
    pass
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/direct/inbox')]"))).click()

for user,message in zip(users,messages):
    time.sleep(5)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class = "x6s0dn4 x78zum5 xdt5ytf xl56j7k"]'))).click()
    time.sleep(random.randrange(3,4))
    browser.find_element(By.NAME,'queryBox').send_keys(user)
    time.sleep(random.randrange(8,10))
    browser.find_element(By.XPATH,'//div[@class ="x9f619 x1n2onr6 x1ja2u2z x1qjc9v5 x78zum5 xdt5ytf x1iyjqo2 xl56j7k xeuugli"]').click()
    time.sleep(random.randrange(3,4))
    browser.find_element(By.XPATH,'//div[@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x9bdzbf x1ypdohk x78zum5 x1i0vuye x1f6kntn xwhw2v2 xl56j7k x17ydfre x1n2onr6 x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 xn3w4p2 x5ib6vp xc73u3c x1tu34mt xzloghq"]').click()
    time.sleep(random.randrange(3,4))
    textarea = browser.find_element(By.XPATH,'//div[@aria-label="Message" and @role="textbox"]')
    textarea.send_keys(message)
    time.sleep(random.randrange(3,4))
    textarea = browser.find_element(By.XPATH,"//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37 xfs2ol5' and text()='Send']").click()
    print(message," sent successfully to",user)
    blacklist.append(user)

df = pd.DataFrame({'Username': blacklist})  # You can specify a column name
df.to_excel(blacklist_file,index=False)
time.sleep(2)
browser.quit()