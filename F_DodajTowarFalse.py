from selenium import webdriver
import time

driver = webdriver.Firefox()
dostawca_list=["ABC0", "8888", "Klient0101"]

for i in range(len(dostawca_list)):
    driver.get("http://localhost:8082/home")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/div').click()

    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/i').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div/div/div').click()
    time.sleep(2)

    try:
        driver.find_element_by_xpath(
            '/html/body/div[9]/div/div/div/div/div[4]/div/div/div[3]/div/div/div/div/input').send_keys(dostawca_list[i])
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/div').click()
        print("OK!")
        driver.close()
    except:
        #print("An exception occurred")
        pass

time.sleep(2)
driver.close()
