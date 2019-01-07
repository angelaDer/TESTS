from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://localhost:8082/home")

xpath_list=['/html/body/div[1]/div/div/ul/li[2]',
            '/html/body/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/div']

dostawca_list=["Klient 1", "Klient 2", "Klient 4"]
towar_list=["Marchew", "marchew", "maRCHew"]

for i in range(len(xpath_list)):
    time.sleep(2)
    driver.find_element_by_xpath(xpath_list[i]).click()

for i in range(len(dostawca_list)):
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/i').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div/div/div').click()
    time.sleep(2)

    driver.find_element_by_xpath(
        '/html/body/div[9]/div/div/div/div/div[4]/div/div/div[3]/div/div/div/div/input').send_keys(dostawca_list[i])
    driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]').click()
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/div').click()
    driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div/div[4]/div/div/div[3]/div/div/div/div/input').send_keys(towar_list[i])

    time.sleep(2)
    elem = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[3]/div/div/div/div/i')

    action = ActionChains(driver)
    action.move_to_element_with_offset(elem, -45, 245).click().perform()
    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div/div/input').send_keys('10')
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div').click()

time.sleep(2)
driver.close()
