from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeDriverManager

import time


# driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver = webdriver.Ie(IEDriverManager().install())
# driver = webdriver.Edge(EdgeDriverManager().install())
# driver = webdriver.Edge(EdgeDriverManager().install())


driver.get("http://google.com")

driver.find_element_by_name("q").send_keys("Automation")

time.sleep(1)

driver.find_element_by_name("btnK").click()

driver.close()
driver.quit()