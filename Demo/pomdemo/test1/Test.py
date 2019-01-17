from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from pomdemo.pages1.homepage import HomePage
from pomdemo.pages1.loginpage import LoginPage
import HtmlTestRunner

class Login(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        
        
    def test_login_valid(self):
        driver = self.driver
        
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()








    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print ("Test completed...")
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../pomdemo/reports"))
#       unittest.main(testRunner=HTMLTestRunner.HTMLT(output='D:/Desktop/Workspaces/EclipsePhoton2Workspace/Demo/reports'))
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/Desktop/Workspaces/EclipsePhoton2Workspace/Demo/pomdemo/reports"))
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\Desktop\Workspaces\EclipsePhoton2Workspace\Demo\reports'))   
    




