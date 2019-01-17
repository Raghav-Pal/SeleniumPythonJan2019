from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.set_page_load_timeout(1)
driver.get("http://google.com")

driver.find_element_by_name("q").send_keys("Automation")

time.sleep(1)

driver.find_element_by_name("btnK").click()

driver.close()
driver.quit()