from pomdemo.locators.Locators import Locators

class LoginPage:
    
    def __init__(self,driver):
        self.driver = driver
        
        self.textbox_username_id = Locators.textbox_username_id
        self.textbox_password_id = "txtPassword"
        self.button_login_id = "btnLogin"
        
    def enter_username(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
        
    def click_login(self):
        self.driver.find_element_by_id(self.button_login_id).click()