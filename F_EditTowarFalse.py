from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

dostawca_list=["Klient 3", "Klient 1", "Klient 5"]
towar_list=["Por", "Pietruszka", "Kapusta"]
data=["dowolna", "2017-03-11", "2016-10-22"]
cena=["10", "dowolna", "9.91"]
ilosc=["22", "93", "dowolna"]

for i in range(len(dostawca_list)):
    driver.get("http://localhost:8082/home")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[3]/div/div').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/div[4]/div').click()
    time.sleep(2)

    driver.find_element_by_xpath(
        '/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div/div/div').click()
    time.sleep(2)

    try:
        driver.find_element_by_xpath(
            '/html/body/div[9]/div/div/div/div/div[4]/div/div/div[3]/div/div/div/div/input').send_keys(dostawca_list[i])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/div').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div/div[4]/div/div/div[3]/div/div/div/div/input').send_keys(towar_list[i])

        time.sleep(2)
        elem = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[3]/div/div/div/div/i')

        action = ActionChains(driver)
        action.move_to_element_with_offset(elem, -45, 245).click().perform()
        time.sleep(2)

        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/input').clear()
        time.sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/input').send_keys(cena[i])

        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div/div/input').clear()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div/div/input').send_keys(ilosc[i])
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div/input').clear()
        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div/input').send_keys(data[i])
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div').click()
        time.sleep(3)
    except:
        pass

time.sleep(2)
driver.close()
