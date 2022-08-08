import time

from Config.config import Testdata
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class HomePage(BasePage):
    Users = (By.XPATH, "//p[normalize-space()='Users']")
    Organization = (By.XPATH, "//p[normalize-space()='Organization']")
    Team = (By.XPATH, "//p[normalize-space()='Team']")
    Reports = (By.XPATH, "//p[normalize-space()='Reports']")
    Planner_Requests = (By.XPATH, "//p[normalize-space()='Planner Requests']")
    Conference_Sync_Status = (By.XPATH, "//p[normalize-space()='Conference Sync Status']")
    Terms_of_Service = (By.XPATH, "//p[normalize-space()='Terms of Service']")
    Privacy_Policy = (By.XPATH,"//p[normalize-space()='Privacy Policy']")
    Send_Dashboard = (By.XPATH,"//p[normalize-space()='Send Dashboard']")
    Logout_dropdown = (By.XPATH, "//li[@class='dropdown header-dropdown']")
    Logout = (By.XPATH, "//a[normalize-space()='Logout']")
    Export_Users = (By.LINK_TEXT, "Export Users")


    '''''Organization elements locators'''
    Create_New_btn=(By.XPATH, "//a[normalize-space()='Create New']")
    '''Create new Organization locators'''
    Organization_name = (By.ID, "org_name")
    Is_active_Checkbox= (By.ID, "is_active")
    Internal_checkbox = (By.ID, "is_internal")
    Create_btn = (By.XPATH, "//button[normalize-space()='Create']")
    Cancel_btn = (By.XPATH, "//a[normalize-space()='Cancel']")
    Edit_org_btn = (By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[6]/a[1]")
    Dashboard_back_btn = (By.XPATH, "//a[normalize-space()='Dashboard']")

    '''Team'''
    Select_Organization = (By.XPATH, "//span[@id='select2-avail-organization-container']")
    Select_Organization_dropdown = ("//ul[@id='select2-avail-organization-results']")
    Select_Organization_textbox = (By.XPATH, "//input[@role='textbox']")
    Team_Name = (By.ID, "name")
    Customer_Contact = (By.ID, "admins")
    Account_Manager = (By.ID, "account_manager")
    Email_conference_checkbox = (By.XPATH,"//input[@name='conference_email_notification']")
    Email_abstract_checkbox = (By.XPATH, "//input[@name='abstract_email_notification']")
    Select_conference = (By.XPATH, "//span[@id='select2-avail-conference-container']")
    Select_conference_Search_box = (By.XPATH, "//input[@role='textbox']")
    Purchase_date = (By.XPATH, "//input[@id='purchase_date']")
    Date_selection = (By.XPATH, "//a[normalize-space()='27']")
    Purchase_date_btn = (By.XPATH, "//button[@id='add-selected-conference']")
    Syndicated_checkbox = (By.XPATH, "//input[@name='syndicate[]']")
    Customized_checkbox = (By.XPATH, "//input[@name='customized[]']")
    Delete_Conference = (By.XPATH, "//span[@class='remove glyphicon glyphicon-trash pull-right']")
    Add_comment = (By.XPATH, "//textarea[@id='comments']")
    Select_year = (By.CSS_SELECTOR, ".ui-datepicker-year")
    Select_month = (By.CSS_SELECTOR, ".ui-datepicker-month")
    Select_date_today = (By.XPATH, '//td[@class=" ui-datepicker-days-cell-over  ui-datepicker-today"]')
    Next_date_picker_arrow = (By.XPATH, "//a[@title='Next']")

    '''Users'''
    Email = (By.ID,"email")
    First_name = (By.ID,"first_name")
    Middle_name= (By.ID,"middle_name")
    Last_name= (By.ID,"last_name")
    Select_Roles= (By.XPATH,"//option[@value='1'][normalize-space()='Larvol']")
    Password= (By.ID,"password")
    Confirm_password= (By.ID,"password_confirmation")
    Select_organization_for_user= (By.XPATH,"//select[@name='org_id']")
    Select_team_for_user= (By.CSS_SELECTOR, "#select2-avail-teams-container")
    Search_box_Team = (By.XPATH, "//input[@role='textbox']")
    #Search_Team_list = (By.XPATH,"//ul[@id='select2-avail-teams-results']")
    ADD_btn = (By.XPATH, "//button[@id='add-selected-team']")
    Next_btn = (By.XPATH, "//button[normalize-space()='Next']")
    Create_user_btn = (By.XPATH, "//button[normalize-space()='Create']")

    '''send dashboard'''
    Select_Conference_Iteration = (By.XPATH, "//b[@role='presentation']")
    Select_Conference_Iteration_textbox = (By.XPATH, "//input[@role='textbox']")
    Syndicated_radio_btn = (By.XPATH, "//label[normalize-space()='Syndicated']")
    Customized_radio_btn = (By.XPATH, "//label[normalize-space()='Customized']")
    Show_Associated_Teams = (By.XPATH, "//button[normalize-space()='Show Associated Teams']")
    Manual_button = (By.ID, "inlineRadio4")
    Mail_subject = (By.ID, "exampleInputEmail1")
    Mail_body = (By.XPATH, "//div[@class='ql-editor ql-blank']//p")
    Choose_upload = (By.XPATH, "//input[@id='attachment']")
    Team_name_checkbox = (By.XPATH, "//td[normalize-space()='Engineering']")
    Team_textbox = (By.XPATH, "//input[@value = '36']")
    Send_Planner_btn = (By.XPATH, "//button[normalize-space()='Send Planner']")
    Send_Email_Accept = (By.XPATH, "//button[normalize-space()='Yes']")
    choose_file_uploader = (By.XPATH, '//div[@class = "fileuploader-input-caption"]//span')
    Team_Table = (By.XPATH, '//div[@class="table teamDetailsTable"]//tbody/tr[]')
    No_Team_Alert = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")



    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(Testdata.BASE_URL)

    def Create_Organzation(self):
        self.do_click(self.Organization)
        self.do_click(self.Create_New_btn)
        self.do_send_keys(self.Organization_name,Testdata.Organization_Name_data)
        self.do_click(self.Create_btn)
        #self.is_visible(Testdata.Organization_Name_data)
        return self.do_click(self.Dashboard_back_btn)

    def Create_Team(self):
        self.do_click(self.Team)
        self.do_click(self.Create_New_btn)
        self.do_click(self.Select_Organization)
        self.do_send_keys(self.Select_Organization_textbox, Testdata.Organization_Name_data)
        time.sleep(5)
        self.click_enter(self.Select_Organization_textbox)
        time.sleep(3)
        self.do_send_keys(self.Team_Name, Testdata.Team_Name_data)
        self.do_send_keys(self.Customer_Contact, Testdata.Customer_contact_data)
        self.do_click(self.Select_conference)
        self.do_send_keys(self.Select_conference_Search_box, Testdata.Conference_Name_data)
        time.sleep(6)
        self.click_enter(self.Select_conference_Search_box)
        self.do_click(self.Purchase_date)
        self.select_date(self.Select_date_today)
        #self.do_click(self.Select_date_today)
        time.sleep(6)
        self.do_click(self.Purchase_date_btn)
        time.sleep(6)
        self.do_click(self.Syndicated_checkbox)
        self.do_click(self.Customized_checkbox)
        self.do_send_keys(self.Add_comment, Testdata.Comment_data)
        time.sleep(6)
        self.do_click(self.Create_btn)
        time.sleep(6)
        return self.do_click(self.Dashboard_back_btn)

    def Create_User(self):
        self.do_click(self.Users)
        self.do_click(self.Create_New_btn)
        self.do_send_keys(self.Email, Testdata.User_email)
        self.do_send_keys(self.First_name, Testdata.FirstName)
        self.do_send_keys(self.Middle_name, Testdata.MiddleName)
        self.do_send_keys(self.Last_name, Testdata.LastName)
        time.sleep(3)
        self.do_click(self.Select_Roles)
        self.do_send_keys(self.Password, Testdata.Password_User)
        self.do_send_keys(self.Confirm_password, Testdata.Password_User)
        time.sleep(6)
        self.do_click(self.Select_organization_for_user)
        self.select_dropdown(self.Select_organization_for_user, Testdata.Organization_Name_data)
        #self.click_enter(self.Select_organization_for_user)
        time.sleep(3)
        self.do_click(self.Select_team_for_user)
        self.do_send_keys(self.Search_box_Team, Testdata.Team_Name_data)
        self.click_enter(self.Search_box_Team)
        time.sleep(3)
        self.do_click(self.ADD_btn)
        self.do_scroll_up()
        time.sleep(3)
        self.do_click(self.Create_user_btn)
        time.sleep(3)
        return self.do_click(self.Dashboard_back_btn)

    def send_automated_email_send_dashboard(self):
        self.do_click(self.Send_Dashboard)
        self.do_click(self.Select_Conference_Iteration)
        self.do_send_keys(self.Select_Conference_Iteration_textbox, Testdata.Conference_Name_data)
        time.sleep(5)
        self.click_enter(self.Select_Conference_Iteration_textbox)
        time.sleep(5)
        self.do_click(self.Syndicated_radio_btn)
        self.do_click(self.Show_Associated_Teams)
        time.sleep(5)
        self.do_click(self.Team_textbox)
        self.do_click(self.Send_Planner_btn)
        time.sleep(5)
        self.do_click(self.Send_Email_Accept)
        time.sleep(5)
        self.back_driver()
        time.sleep(5)


    def send_customized_manual_email_send_dashboard(self):
        self.do_click(self.Send_Dashboard)
        self.do_click(self.Select_Conference_Iteration)
        self.do_send_keys(self.Select_Conference_Iteration_textbox, Testdata.Conference_Name_data)
        time.sleep(5)
        self.click_enter(self.Select_Conference_Iteration_textbox)
        time.sleep(5)
        self.do_click(self.Customized_radio_btn)
        self.do_click(self.Show_Associated_Teams)
        time.sleep(5)
        # self.do_click(self.Choose_upload)
        # time.sleep(5)
        # self.do_send_keys(self.Choose_upload, "/Users/mayurisurwade/sample-pdf-file.pdf")
        # time.sleep(5)
        self.do_click(self.Manual_button)
        self.do_send_keys(self.Mail_subject, Testdata.Mail_Subject)
        self.do_send_keys(self.Mail_body, Testdata.Mail_Body)
        # Row_lenght = self.find_element(self.Team_Table)
        # Row_Count = len(Row_lenght)
        # print(Row_Count)
        self.do_click(self.Team_textbox)
        self.do_click(self.Send_Planner_btn)
        time.sleep(5)
        self.do_click(self.Send_Email_Accept)
        time.sleep(5)
        self.back_driver()
        time.sleep(5)

    def Logout_admin_panel(self):
        self.do_click(self.Logout_dropdown)
        self.do_click(self.Logout)

    def send_customized_manual_email_without_clicking_on_Team_checkbox(self):
        self.do_click(self.Send_Dashboard)
        self.do_click(self.Select_Conference_Iteration)
        self.do_send_keys(self.Select_Conference_Iteration_textbox, Testdata.Conference_Name_data)
        time.sleep(5)
        self.click_enter(self.Select_Conference_Iteration_textbox)
        time.sleep(5)
        self.do_click(self.Customized_radio_btn)
        self.do_click(self.Show_Associated_Teams)
        time.sleep(5)
        # self.do_click(self.Choose_upload)
        # time.sleep(5)
        # self.do_send_keys(self.Choose_upload, "/Users/mayurisurwade/sample-pdf-file.pdf")
        # time.sleep(5)
        self.do_click(self.Manual_button)
        self.do_send_keys(self.Mail_subject, Testdata.Mail_Subject)
        self.do_send_keys(self.Mail_body, Testdata.Mail_Body)
        # Row_lenght = self.find_element(self.Team_Table)
        # Row_Count = len(Row_lenght)
        # print(Row_Count)
        self.do_click(self.Send_Planner_btn)
        time.sleep(5)
        self.do_click(self.Send_Email_Accept)
        time.sleep(5)
        self.back_driver()
        time.sleep(5)







































