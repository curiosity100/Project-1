import sys
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


# to create a account for user with login account
# USER DETAILS
# name ="mathew conway", ID =1230, job ="software engineer", role="professional", sub-unit="Adminstration", location="HQ - CA, USA, jobtype="freelance"

def test_code_1():
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(url)

    # Login
    WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "// input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    # To Add New User
    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
    time.sleep(3)

    # First name and Last name
    driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("mathew")
    driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("conway")

    # Id
    driver.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@class='oxd-input oxd-input--active']").click()
    driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").send_keys(1230)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)

    # to add job details
    driver.find_element(By.LINK_TEXT, "Job").click()
    time.sleep(3)
    # to select software engineer
    driver.find_element(By.XPATH, "//form/div[1]/div/div[2]/div/div[2]/div/div").click()
    driver.find_element(By.XPATH, ("//*[contains(text(), 'Software Engineer')]")).click()

    # to select professional
    driver.find_element(By.XPATH, "//form/div[1]/div/div[4]/div/div[2]/div/div/div[1]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Professionals')]").click()
    # to select sub unit
    driver.find_element(By.XPATH, "//form/div[1]/div/div[5]/div/div[2]/div/div").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Administration')]").click()
    # to select location
    driver.find_element(By.XPATH, "//form/div[1]/div/div[6]/div/div[2]/div/div/div[1]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'HQ - CA, USA')]").click()
    # to select job type
    driver.find_element(By.XPATH, "//form/div[1]/div/div[7]/div/div[2]/div/div/div[1]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Freelance')]").click()
    time.sleep(3)
    # to save
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # to get employee details screenshot
    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(3)
    #emp id
    driver.find_element(By.XPATH, "//form/div[1]/div/div[2]/div/div[2]/input").send_keys(1230)
    time.sleep(3)
    # to click search
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    # to take screenshot of employee details
    employee_details = driver.find_element(By.XPATH, "//div[@class='orangehrm-container']")
    driver.execute_script("arguments[0].scrollIntoView()", employee_details)
    time.sleep(3)
    driver.save_screenshot("employee-details.png")

    # Go to Admin Section
    driver.find_element(By.LINK_TEXT, "Admin").click()
    time.sleep(3)

    # to Create New User
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='oxd-button oxd-button--medium oxd-button--secondary']")))
    driver.find_element(By.XPATH,"//button[@type='button' and @class='oxd-button oxd-button--medium oxd-button--secondary']").click()
    time.sleep(3)
    # user role
    user_role = driver.find_element(By.XPATH, "//form/div[1]/div/div[1]/div/div[2]/div")
    user_role.click()
    # admin
    driver.find_element(By.XPATH, "//*[contains(text(), 'Admin')]").click()
    # status
    status = driver.find_element(By.XPATH, "//form/div[1]/div/div[3]/div/div[2]/div/div")
    status.click()
    # enabled
    driver.find_element(By.CSS_SELECTOR, "div.oxd-select-option:nth-child(2)").click()
    # employee name autocomplete box
    driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("conway")
    time.sleep(5)
    names = driver.find_elements(By.XPATH, "//div[@class='oxd-autocomplete-wrapper']/div[2]/div")
    for i in names:
        if i.text == 'mathew conway':
            i.click()
            break
    else:
        sys.exit("user name not found, please try again")

    # username
    driver.find_element(By.XPATH,"//div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[4]/div/div[2]/input").send_keys("mathew")

    # to create password
    driver.find_element(By.CSS_SELECTOR,".user-password-cell > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("qwAS@3456")
    driver.find_element(By.XPATH,"//div[@class='oxd-form-row user-password-row']//div[1]//div[2]//div[1]//div[2]//input").send_keys("qwAS@3456")
    time.sleep(5)
    # To click save
    driver.find_element(By.XPATH, "//div[@class='oxd-form-actions']//button[@type='submit']").click()
    time.sleep(10)

    # to search in admin section
    driver.find_element(By.LINK_TEXT, "Admin").click()
    time.sleep(3)
    # username
    driver.find_element(By.CSS_SELECTOR, "input.oxd-input:nth-child(1)").send_keys("mathew")
    # user role - Admin
    driver.find_element(By.XPATH, "//div[@class='oxd-form-row']//div[1]//div[2]//div[2]//div[1]").click()
    driver.find_element(By.CSS_SELECTOR, "div.oxd-select-option:nth-child(2)").click()
    # employee name autocomplete box
    driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("conway")
    time.sleep(5)
    names = driver.find_elements(By.XPATH, "//div[@class='oxd-autocomplete-wrapper']/div[2]/div")
    for i in names:
        if i.text == 'mathew conway':
            i.click()
            break
    else:
        sys.exit("user name not found, please try again")

    # to select enabled from dropdown box
    driver.find_element(By.XPATH,"//div[@class='oxd-grid-4 orangehrm-full-width-grid']/div[4]/div/div[2]/div/div").click()
    driver.find_element(By.CSS_SELECTOR, "div.oxd-select-option:nth-child(2)").click()
    time.sleep(2)
    # to click search
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # to verify
    total_record = driver.find_element(By.XPATH,"//div[@class='orangehrm-background-container']/div[2]/div[2]/div/span")
    if total_record.text == "(1) Record Found":
        username = driver.find_element(By.XPATH, "//div[@class='orangehrm-container']/div/div[2]/div/div/div[2]")
        employeename = driver.find_element(By.XPATH, "//div[@class='orangehrm-container']/div/div[2]/div/div/div[4]")
        if username.text == "mathew" and employeename.text == "mathew conway":
            print("user is created and it is verified")
            driver.execute_script("arguments[0].scrollIntoView()", employeename)
            time.sleep(3)
            driver.save_screenshot("user-record.png")
            # to logout
            driver.find_element(By.XPATH, "//li[@class='oxd-userdropdown']").click()
            time.sleep(2)
            driver.find_element(By.LINK_TEXT, "Logout").click()
            # to login using created profile
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
            driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("mathew")
            driver.find_element(By.XPATH, "// input[@placeholder='Password']").send_keys("qwAS@3456")
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print("user log-in verified")

        else:
            print("Username is not found, please try again")
    else:
        print("user record does not match, please try again")


#after successful completion (to delete the user)
def test_code_2():
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(url)

    # Login
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "// input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    # to get employee details screenshot
    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(3)
    # emp id
    driver.find_element(By.XPATH, "//form/div[1]/div/div[2]/div/div[2]/input").send_keys(1230)
    time.sleep(3)
    # to click search
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    # to delete employee details
    employee_details = driver.find_element(By.XPATH, "//div[@class='orangehrm-container']")
    driver.execute_script("arguments[0].scrollIntoView()", employee_details)
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@data-v-9971f952='' and @data-v-77b08b9a='']/div[9]/div/button[1]").click()
    driver.find_element(By.XPATH, "//div[@class='oxd-dialog-container-default--inner']/div/div[3]/button[2]").click()
    time.sleep(8)
    # to verify
    total_record = driver.find_element(By.XPATH,"//div[@class='orangehrm-background-container']/div[2]/div[2]/div/span")
    if total_record.text == "No Records Found":
        print("Employee details deleted successfully")
    else:
        print("Employee details not deleted,Please verify")
