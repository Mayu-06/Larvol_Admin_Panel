from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

from Config.config import Testdata

'''This class is the parent of all pages'''
'''It contains all generic methods and utilities for all the pages'''


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        driver.maximize_window()

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def find_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        return self.driver.title

    def select_dropdown(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        select = Select(element)
        select.select_by_visible_text(text)

    def do_scroll_down(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")

    def do_scroll_up(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    def do_scroll_into_view_element(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def dismiss_alert(self):
        WebDriverWait(self.driver, 10).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def Accept_alert(self):
        WebDriverWait(self.driver, 10).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def back_driver(self):
        self.driver.back()
        time.sleep(2)

    def forward_driver(self):
        self.driver.forward()
        time.sleep(2)

    def mouse_hover(self, by_locator):
        ele = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(by_locator))
        act_chains = ActionChains(self.driver)
        act_chains.move_to_element(ele).perform()

    def New_login_tab(self):
        self.driver.execute_script("window.open('https://www.flipkart.com/account/login?ret=/');")

    def switch_to_new_tab(self):
        p = self.driver.current_window_handle
        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)

    def select_Jquery_dropdown(self, by_locator, value):
        list = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator))
        print(list)
        for ele in list:
            if ele.text == value:
                return ele.click()


    def clear_text_field(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator))
        i = 6
        while i > 0:
            element.send_keys(Keys.BACK_SPACE)
            if (i == 0):
                break
            i = i - 1

    def click_enter(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator))
        return element.send_keys(Keys.ENTER)

    def select_year(self,by_locator, by_locator1):
        element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator))
        while (element.text == Testdata.Year):
            self.do_click(by_locator1)
            continue
        else:
            pass

    def select_month(self,by_locator, by_locator1):
        element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator))
        while (element.text == Testdata.Month):
            self.do_click(by_locator1)
            continue
        else:
            pass

    def select_date(self, by_locator):
        self.do_click(by_locator)







