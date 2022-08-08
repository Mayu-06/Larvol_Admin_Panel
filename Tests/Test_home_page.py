from Config.config import Testdata
from Tests.Test_base import BaseTest
from Pages.login_page import LoginPage
from Pages.base_page import BasePage
import pytest


class Test_Homepage(BaseTest):

    def test_create_new_Organizations(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(Testdata.USERNAME, Testdata.PASSWORD)
        homepage.Create_Organzation()
        homepage.Create_Team()
        homepage.Create_User()
        homepage.send_automated_email_send_dashboard()
        homepage.Logout_admin_panel()

    # def test_create_new_Team(self):
    #     self.loginpage = LoginPage(self.driver)
    #     homepage = self.loginpage.do_login(Testdata.USERNAME, Testdata.PASSWORD)
    #     homepage.Create_Team()

    # def test_create_new_User(self):
    #     self.loginpage = LoginPage(self.driver)
    #     homepage = self.loginpage.do_login(Testdata.USERNAME, Testdata.PASSWORD)
    #     homepage.Create_User()

    # def test_automated_sendtron(self):
    #     self.loginpage = LoginPage(self.driver)
    #     homepage = self.loginpage.do_login(Testdata.USERNAME, Testdata.PASSWORD)
    #     homepage.send_automated_email_send_dashboard()
    #
    # def test_Logout(self):
    #     self.loginpage = LoginPage(self.driver)
    #     homepage = self.loginpage.do_login(Testdata.USERNAME, Testdata.PASSWORD)
    #     homepage.Logout_admin_panel()

    def test_manual_sendtron(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(Testdata.USERNAME, Testdata.PASSWORD)
        #homepage.send_customized_manual_email_send_dashboard()
        homepage.send_customized_manual_email_without_clicking_on_Team_checkbox()
        print("Test failed, Please click on Team Name")


