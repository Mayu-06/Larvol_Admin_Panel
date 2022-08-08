#import export as export
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#from Config.config import Testdata


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        '''This three line option code is to disable the line of Chrome is being controlled by automated software'''
        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        prefs = {"credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        web_driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        web_driver.implicitly_wait(10)


    if request.param == "safari":
        web_driver = webdriver.Safari()
    request.cls.driver = web_driver

    yield
    web_driver.quit()
