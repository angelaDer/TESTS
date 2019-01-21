from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:9999/login")

driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[1]'
                             '/div/div/div/div/div/input').send_keys('klient1')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[2]'
                             '/div/div/div/div/div/input').send_keys('123')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/span').click()

