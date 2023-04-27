from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"user-name").send_keys("locked_out_user")
time.sleep(2)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID,"login-button").click()
time.sleep(15)