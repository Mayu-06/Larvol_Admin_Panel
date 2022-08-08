from Config.config import Testdata
from Pages.home_page import HomePage
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    EMAIL = (By.ID,'username')
    PASSWORD = (By.ID,'password')
    Login_btn= (By.XPATH,"//button[contains(text(),'Login')]")
    Remember_Me = (By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/div[1]/label[1]")
    Forgot_password_link = (By.XPATH,"//a[contains(text(),'Forgot Your Password?')]")
    Users= (By.XPATH,"//p[normalize-space()='Users']")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(Testdata.BASE_URL)

    def get_login_page_title(self,title):
        return self.get_title(title)

    def is_Forgot_password_link_visible(self):
        return self.is_visible(self.Forgot_password_link)

    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.Login_btn)
        self.is_visible(self.Users)
        return HomePage(self.driver)
