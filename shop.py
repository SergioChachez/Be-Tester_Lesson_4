import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
shop = driver.find_element_by_id("menu-item-40")
shop.click()
html_5_webapp = driver.find_element_by_css_selector("[data-product_id='182']")
html_5_webapp.click()
item = driver.find_element_by_css_selector("[id='wpmenucartli'] :nth-child(2)")
item_get_text = item.text
assert item_get_text == "1 item"
price = driver.find_element_by_css_selector("#wpmenucartli :nth-child(3)")
price_get_text = price.text
assert price_get_text == "180.00"
cart = driver.find_element_by_css_selector("[title='View your shopping cart']")
cart.click()
subtotal = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-subtotal")))
total = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".order-total")))
driver.quit()



