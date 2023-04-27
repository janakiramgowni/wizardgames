from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID,"login-button").click()
time.sleep(5)
element = driver.find_element(By.CLASS_NAME,"product_sort_container")
drop = Select(element)
#select by visisble text
drop.select_by_index(2)
time.sleep(15)
driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()
time.sleep(20)
driver.find_element(By.CLASS_NAME,"shopping_cart_badge").click()
driver.find_element(By.ID,"checkout").click()
driver.find_element(By.ID,"first-name").send_keys("JOhn")
driver.find_element(By.ID,"last-name").send_keys("DOE")
driver.find_element(By.ID,"postal-code").send_keys("123")
driver.find_element(By.ID,"continue").click()
time.sleep(3)

