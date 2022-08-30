import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
account = driver.find_element_by_id("menu-item-50")
account.click()
time.sleep(3)
email_address = driver.find_element_by_id("reg_email")
email_address.send_keys("sergio_chachez@gmail.com")
time.sleep(3)
password = driver.find_element_by_id("reg_password")
password.send_keys("#Beckham2019")
time.sleep(3)
register_btn = driver.find_element_by_name("register")
register_btn.click()
time.sleep(3)
driver.quit()


import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
account = driver.find_element_by_id("menu-item-50")
account.click()
time.sleep(3)
username = driver.find_element_by_id("username")
username.send_keys("sergio_chachez@gmail.com")
time.sleep(3)
password1 = driver.find_element_by_id("password")
password1.send_keys("#Beckham2019")
time.sleep(3)
login_btn = driver.find_element_by_name("login")
login_btn.click()
time.sleep(3)
logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation :nth-child(6)")
if logout is None:
    print("Logout Отсутствует")
else:
    print("Logout Есть")
time.sleep(3)
driver.quit()
