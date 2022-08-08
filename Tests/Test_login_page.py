import time

from Config.config import Testdata
from Pages.login_page import LoginPage
import pytest
from Tests.Test_base import BaseTest


class Test_Login(BaseTest):
    def test_forgot_password_link(self):
        self.loginpage= LoginPage(self.driver)
        flag=self.loginpage.is_Forgot_password_link_visible()
        assert flag

    def test_page_title(self):
        self.loginpage= LoginPage(self.driver)
        title=self.loginpage.get_title(Testdata.LOGIN_PAGE_TITLE)
        assert title == Testdata.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(Testdata.USERNAME,Testdata.PASSWORD)
        time.sleep(5)


