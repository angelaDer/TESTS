from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("http://localhost:8082/home")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[3]/div/div').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/i').click()
time.sleep(2)