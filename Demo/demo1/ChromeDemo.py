from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# from selenium.webdriver import ChromeOptions
import time
from selenium.webdriver.firefox import options
from selenium.webdriver.chrome.options import Options

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")

chrome_options = webdriver.ChromeOptions()
chrome_options.addArguments("--headless")

# options.addArguments("--disable-gpu");
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),Options=chrome_options)
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=firefox_options )

driver.get("http://google.com")

print (driver.title)

driver.find_element_by_name("q").send_keys("Automation")

time.sleep(1)

driver.find_element_by_name("btnK").click()

driver.close()
driver.quit()