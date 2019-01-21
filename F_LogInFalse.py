from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://localhost:9999/login")

login_list = ['klient1', 'Klaudia', 'Angela', 'Daniel', 'Ziemniak']
pass_list = ['Lubie', 'nalesniki', 'z', 'dzemem', 'i nutella']

for i in range(len(login_list)):
    time.sleep(1)
    try:
        driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[1]'
                                     '/div/div/div/div/div/input').send_keys(login_list[i])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[2]'
                                     '/div/div/div/div/div/input').send_keys(pass_list[i])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/span').click()
    except:
        pass

time.sleep(2)
driver.close()