from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

driver.get("http://books.toscrape.com/")

element = driver.find_element(By.NAME, "q")

element.click()

time.sleep(10)
driver.quit()
