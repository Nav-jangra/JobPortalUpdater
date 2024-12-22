import time

from datetime import datetime
from selenium.webdriver.common.by import By

from config.config import load_config
from utils.utils import log_msg,catch ,GetElement,is_element_present,WaitTillElementPresent


def shineLogin(driver):
    """Login to Shine.in"""
    config = load_config()
    username = config.get("shine",{}).get("username","")  
    password = config.get("shine",{}).get("password","")
    status = False 
    driver = driver
    username_locator = "id_email_login"
    password_locator = "id_password"
    login_btn_locator = "//button[contains(text(),'Login')]"
    shineUrl = "https://www.shine.com/myshine/login/"

    try:
        driver.get(shineUrl)
        print(driver.title.lower())
        if "shine" in driver.title.lower():
            log_msg("Website Loaded Successfully.")

        emailFieldElement = None
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
            if WaitTillElementPresent(driver, login_btn_locator, "XPATH", 10):
                GetElement(driver, login_btn_locator, "XPATH").click()
        else:
            log_msg("None of the elements found to login.")

        if emailFieldElement is not None:
            # CheckPoint to verify login
            if WaitTillElementPresent(driver, "container_dashboard_left", locator="CLASS", timeout=40):
                CheckPoint = GetElement(driver, "container_dashboard_left", locator="CLASS")
                if CheckPoint:
                    log_msg("Shine Login Successful")
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

def shineUpdateProfile(driver):
    try:
        edit_work_locator = "edit-icon-work-summary-web"
        save_button  = "id-save-worksummary-web"
        close_popup = "//button[contains(text(),'Visit Profile')]"

        driver.get("https://www.shine.com/myshine/myprofile/")

        #closing the popup for profile save
        if WaitTillElementPresent(driver, close_popup, "XPATH", 10):
            popup = GetElement(driver, close_popup, locator="XPATH")
            if(popup):
                popup.click()
            time.sleep(2)
        
        time.sleep(5)
        #locating the edit profile button
        WaitTillElementPresent(driver, edit_work_locator, "ID", 10)
        profElement = GetElement(driver, edit_work_locator, locator="ID")
        profElement.click()
        driver.implicitly_wait(2)
        
        #saving the tab
        WaitTillElementPresent(driver, save_button, "ID", 10)
        profElement = GetElement(driver, save_button, locator="ID")
        profElement.click()
        driver.implicitly_wait(2)
        time.sleep(5)
    
    except Exception as e:
        catch(e)

def shineUploadResume(driver, resumePath):
    try:
        attachCVID = "up_new_resume"
        CheckPointXpath = "id_file"
        saveXpath = "//*[contains(@class, 'resumeupload')]"
        close_profile_updater = "//*[contains(@class, 'mobileskipbtn')]"
        close_popup = "//button[contains(text(),'Visit Profile')]"
        update_time = "//*[contains(@class, 'score_checker')]"

        driver.get("https://www.shine.com/myshine/myprofile/")

        #remove popup profile not updated
        if WaitTillElementPresent(driver, close_popup, "XPATH", 10):
            GetElement(driver, close_popup, locator="XPATH").click()
            time.sleep(2)
        
        #founding the element upload resume
        if WaitTillElementPresent(driver, attachCVID, "ID", 10):
            GetElement(driver, attachCVID, locator="ID").click()
            time.sleep(2)

        #giving resume path
        WaitTillElementPresent(driver, CheckPointXpath, locator="ID", timeout=10)
        AttachElement = GetElement(driver, CheckPointXpath, locator="ID")
        AttachElement.send_keys(resumePath)

        # submitting the resume
        if WaitTillElementPresent(driver, saveXpath, locator="XPATH", timeout=5):
            saveElement = GetElement(driver, saveXpath, locator="XPATH")
            saveElement.click()

        #closing the popup
        if WaitTillElementPresent(driver, close_profile_updater, locator="XPATH", timeout=5):
            saveElement = GetElement(driver, close_profile_updater, locator="XPATH")
            saveElement.click()

        #removing previous resumes
        # class="cls_delete resume_change"
        #id_cpSubmit
        
        #checking if resume uploaded succesfull
        WaitTillElementPresent(driver, update_time, locator="XPATH", timeout=5)
        CheckPoint = GetElement(driver, update_time, locator="XPATH")
        if CheckPoint:
            LastUpdatedDate = CheckPoint.text
            todaysDate1 = datetime.today().strftime("%b. %d, %Y,")
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
