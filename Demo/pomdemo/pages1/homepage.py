class HomePage:
    
    def __init__(self,driver):
        self.driver = driver
        
        self.link_welcome_id = "welcome"
        self.link_logout_linktext = "Logout"
        
    def click_welcome(self):
        self.driver.find_element_by_id(self.link_welcome_id).click()
        
    def click_logout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
        
        
        
    