from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        #super(GoogleSearch, cls).setUpClass()
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_searchForAutomation(self): 
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation")
        time.sleep(1)
        self.driver.find_element_by_name("btnK").click() 
    
        
    def test_searchForPython(self): 
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Python")
        time.sleep(1)
        self.driver.find_element_by_name("btnK").click()  
      
    
    @classmethod
    def tearDownClass(cls):
        #super(GoogleSearch, cls).tearDownClass()
        cls.driver.close()
        cls.driver.quit()
        print ("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/Desktop/Workspaces/EclipsePhoton2Workspace/Demo/reports"))


