from selenium import webdriver
import time
import json
import string
import os
import random


profile = webdriver.FirefoxProfile()
profile.set_preference("dom.disable_open_during_load", False)
web = webdriver.Firefox(firefox_profile=profile)
web.get('https://www.goldstein-invest.com/clientzone/en/live_account_registration/step1')

time.sleep(2)

names = json.loads(open('names.json').read())
chars = string.ascii_letters + string.digits
surname_chars = string.ascii_letters
random_nums = string.digits
countries = ['BE', 'HR', 'KP', 'PA', 'ES', 'TN', 'ZW', 'GN', 'DE', 'HU']
countries_dial = ['+32', '+385', '+850', '+507', '+34', '+216', '+263', '+224', '+49', '+36']

for name in names:
    name_extra = ''.join(random.choice(string.digits))
    random_country = random.randint(0, 9)

    firstName = name
    FNfill = web.find_element_by_xpath('//*[@id="firstname"]')
    FNfill.send_keys(firstName)

    lastName = name
    LSfill = web.find_element_by_xpath('//*[@id="lastname"]')
    LSfill.send_keys(lastName)

    email = name.lower() + name_extra + '@gmail.com'
    emailFill = web.find_element_by_xpath('//*[@id="email"]')
    emailFill.send_keys(email)

    phoneNum = ''.join(random.choice(random_nums) for i in range(8))
    PNFill = web.find_element_by_xpath('//*[@id="phone"]')
    PNFill.send_keys(phoneNum)

    random_date = random.randint(1, 9)
    random_month = random.randint(1, 9)
    random_year = random.randint(1, 9)

    dob = f"0{random_date}/0{random_month}/199{random_year}"
    DOBFill = web.find_element_by_xpath('//*[@id="datepicker"]')
    DOBFill.send_keys(dob)

    pw = ''.join(random.choice(chars) for i in range(8))
    password =  f"{pw}{random.randint(0, 9)}"
    pwFill = web.find_element_by_xpath('//*[@id="password"]')
    pwFill.send_keys(password)

    confPass = web.find_element_by_xpath('//*[@id="confirm_password"]')
    confPass.send_keys(password)

    openAcc = web.find_element_by_xpath('//*[@id="real_form_submit"]')
    openAcc.click()
    print("success")
    web.refresh()
    time.sleep(2)
