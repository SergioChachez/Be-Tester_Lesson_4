import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
account = driver.find_element_by_id("menu-item-50")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("sergio_chachez@gmail.com")
password1 = driver.find_element_by_id("password")
password1.send_keys("#Beckham2019")
login_btn = driver.find_element_by_name("login")
login_btn.click()
shop = driver.find_element_by_id("menu-item-40")
shop.click()
html_5_forms = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']")
html_5_forms.click()
title = driver.find_element_by_css_selector("[itemprop='name']")
title_get_text = title.text
assert title_get_text == "HTML5 Forms"
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
shop = driver.find_element_by_id("menu-item-40")
shop.click()
HTML = driver.find_element_by_link_text("HTML")
HTML.click()
items = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
if len(items) == 3:
    print("отображается 3 товара")
else:
    print("количество товаров: " + str(len(items)))
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
shop = driver.find_element_by_id("menu-item-40")
shop.click()
default = driver.find_element_by_class_name("orderby")
default_check = default.get_attribute("value")
if default_check == "menu_order":
    print("Default Sorting")
else:
    print("Error")
driver.find_element_by_tag_name("select").click()
driver.find_element_by_css_selector("[value='price-desc']").click()
sort = driver.find_element_by_class_name("orderby")
sort_check = sort.get_attribute("value")
if sort_check == "price-desc":
    print("Sort by Price: High to Low")
else:
    print("Error")
driver.quit()



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
account = driver.find_element_by_id("menu-item-50")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("sergio_chachez@gmail.com")
password1 = driver.find_element_by_id("password")
password1.send_keys("#Beckham2019")
login_btn = driver.find_element_by_name("login")
login_btn.click()
shop = driver.find_element_by_id("menu-item-40")
shop.click()
android_guide = driver.find_element_by_css_selector("[title='Android Quick Start Guide']")
android_guide.click()
old_price = driver.find_element_by_css_selector(".price > del > span")
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"
new_price = driver.find_element_by_css_selector(".price > ins > span")
new_price_get_text = new_price.text
assert new_price_get_text == "₹450.00"
cover_book = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
cover_book.click()
cover_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
cover_close.click()
driver.quit()



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
time.sleep(3)
item = driver.find_element_by_css_selector("#wpmenucartli :nth-child(2)")")
item_get_text = item.text
assert item_get_text == "1 item"
price = driver.find_element_by_css_selector("#wpmenucartli :nth-child(3)")
price_get_text = price.text
assert price_get_text == "₹180.00"
cart = driver.find_element_by_css_selector("[title='View your shopping cart']")
cart.click()
subtotal = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-subtotal")))
total = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".order-total")))
driver.quit()



import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_id("menu-item-40")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
book1 = driver.find_element_by_css_selector("[data-product_id='182']")
book1.click()
time.sleep(3)
book2 = driver.find_element_by_css_selector("[data-product_id='180']")
book2.click()
cart = driver.find_element_by_class_name("cartcontents")
cart.click()
time.sleep(3)
remove = driver.find_element_by_css_selector("[data-product_id='182']")
remove.click()
time.sleep(3)
undo = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-message :nth-child(1)")))
undo.click()
quantity = driver.find_element_by_css_selector(".quantity :nth-child(1)")
quantity.clear()
quantity.send_keys("3")
update_basket_btn = driver.find_element_by_css_selector("[value='Update Basket']")
update_basket_btn.click()

time.sleep(3)
apply_coupon_btn = driver.find_element_by_css_selector("[value='Apply Coupon']")
apply_coupon_btn.click()
time.sleep(3)
title = driver.find_element_by_css_selector(".woocommerce-error :nth-child(1)")
title_get_text = title.text
assert title_get_text == "Please enter a coupon code."
driver.quit()


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
driver.execute_script("window.scrollBy(0, 300);")
book = driver.find_element_by_css_selector("[data-product_id='182']")
book.click()
time.sleep(3)
cart = driver.find_element_by_class_name("cartcontents")
cart.click()
time.sleep(3)
checkout_btn = driver.find_element_by_css_selector(".wc-proceed-to-checkout > a")
proceed = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout > a")))
checkout_btn.click()
first = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[autocomplete='given-name']")))
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Sergio")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Chachez")
email_address = driver.find_element_by_id("billing_email")
email_address.send_keys("sergio_chachez@gmail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89658877167")
country = driver.find_element_by_class_name("select2-choice")
country.click()
search_stroke = driver.find_element_by_id("s2id_autogen1_search")
search_stroke.click()
honduras = driver.find_element_by_id("select2-result-label-101")
honduras.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Perspective St.")
city = driver.find_element_by_id("billing_city")
city.send_keys("Sorento")
state = driver.find_element_by_id("billing_state")
state.send_keys("Leninsky District")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("410064")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_payments = driver.find_element_by_css_selector("[value='cheque']")
check_payments.click()
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()
inscription1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "woocommerce-thankyou-order-received")))
inscription2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".method :nth-child(1)")))
driver.quit()



