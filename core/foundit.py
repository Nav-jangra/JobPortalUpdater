import time

from datetime import datetime
from selenium.webdriver.common.by import By

from config.config import load_config
from utils.utils import log_msg,catch ,GetElement,is_element_present,WaitTillElementPresent


def founditLogin(driver):
    """Login to foundit.in"""
    config = load_config()
    username = config.get("foundit",{}).get("username","")  
    password = config.get("foundit",{}).get("password","")
    status = False
    driver = driver
    username_locator = "signInName"
    password_locator = "password"
    login_btn_locator = "signInbtn"
    login_with_Password = "loginWith"
    skip_locator = "acceptAll"
    foundItUrl = "https://www.foundit.in/rio/login"

    try:
        driver.get(foundItUrl)
        print(driver.title.lower())
        if "foundit" in driver.title.lower():
            log_msg("Website Loaded Successfully.")

        emailFieldElement = None
        if WaitTillElementPresent(driver, login_with_Password, "CLASS", 10):
                GetElement(driver, login_with_Password, "CLASS").click()
        if is_element_present(driver, By.ID, username_locator):
            emailFieldElement = GetElement(driver, username_locator, locator="ID")
            time.sleep(1)
            if emailFieldElement is not None:
                emailFieldElement.clear()
                emailFieldElement.send_keys(username)
            passFieldElement = GetElement(driver, password_locator, locator="ID")
            time.sleep(1)
            if passFieldElement is not None:
                passFieldElement.clear()
                passFieldElement.send_keys(password)
            time.sleep(1)
            if WaitTillElementPresent(driver, login_btn_locator, "ID", 10):
                GetElement(driver, login_btn_locator, "ID").click()
        else:
            log_msg("None of the elements found to login.")

        if emailFieldElement is not None:
            # Added click to Skip button
            print("Checking Cookies Button button")

            if WaitTillElementPresent(driver, skip_locator, "ID", 10):
                GetElement(driver, skip_locator, "ID").click()

            # CheckPoint to verify login
            if WaitTillElementPresent(driver, "dashboardTitle", locator="CLASS", timeout=40):
                CheckPoint = GetElement(driver, "dashboardTitle", locator="CLASS")
                if CheckPoint:
                    log_msg("Foundit Login Successful")
                    status = True
                    return (status, driver)
                else:
                    log_msg("Unknown Login Error")
                    return (status, driver)
            else:
                log_msg("Unknown Login Error")
                return (status, driver)

    except Exception as e:
        catch(e)
    return (status, driver)

def UploadResume(driver, resumePath):
    try:
        attachCVID = "inline-resume"
        CheckPointXpath = "//*[contains(@class, 'last-update')]"

        driver.get("https://www.foundit.in/seeker/profile")

        time.sleep(2)
        WaitTillElementPresent(driver, attachCVID, locator="ID", timeout=10)
        AttachElement = GetElement(driver, attachCVID, locator="ID")
        AttachElement.send_keys(resumePath)

        WaitTillElementPresent(driver, CheckPointXpath, locator="XPATH", timeout=30)
        CheckPoint = GetElement(driver, CheckPointXpath, locator="XPATH")
        if CheckPoint:
            LastUpdatedDate = CheckPoint.text
            todaysDate1 = datetime.today().strftime("%d %B %Y")
            todaysDate2 = datetime.today().strftime("%B %#d %Y")
            if todaysDate1 in LastUpdatedDate or todaysDate2 in LastUpdatedDate:
                log_msg(
                    "Resume Document Upload Successful. Last Updated date = %s"
                    % LastUpdatedDate
                )
            else:
                log_msg(
                    "Resume Document Upload failed. Last Updated date = %s"
                    % LastUpdatedDate
                )
        else:
            log_msg("Resume Document Upload failed. Last Updated date not found.")

    except Exception as e:
        catch(e)
    time.sleep(2)
