'''Закончить регистрацию на сайте 'https://dumskaya.net/' с использованием ожиданий которые рассматривали на паре.'''

import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logins import email, nick, password

driver = webdriver.Chrome()
driver.get('https://dumskaya.net/')
driver.maximize_window()

# email = 'qwqwqw@gmail.com'
# nick = 'qwqwqwqw'
# password = '123456'

id_start = 'pp'
button_start = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('id', id_start)))
button_start.click()

xpath_registration_button = '//a[@href="/register/"]'
button_reg = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_registration_button)))
button_reg.click()

xpath_fild_email = '//td/input[@name="email"]'
fild_email = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_fild_email)))
fild_email.send_keys(email)

xpath_fild_nick = '//td/input[@name="nick"]'
fild_nick = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_fild_nick)))
fild_nick.send_keys(nick)

xpath_fild_password = '//td/input[@name="password1"]'
fild_password = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_fild_password)))
fild_password.send_keys(password)

xpath_fild_repeat_password = '//td/input[@name="password2"]'
fild_repeat_password = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(('xpath', xpath_fild_repeat_password)))
fild_repeat_password.send_keys(password)

xpath_gender_button = '//td/input[@value="f"]'
gender_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_gender_button)))
gender_button.click()

xpath_reg_button_finally = '//td/input[@value="Зарегистрироваться"]'
reg_button_finally = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_reg_button_finally)))
reg_button_finally.click()

time.sleep(500)
