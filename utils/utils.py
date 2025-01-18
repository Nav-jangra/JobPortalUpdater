import io
import logging
import os
import sys
import time
from random import choice, randint
from string import ascii_uppercase, digits

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager as CM

from config.config import load_config

logging.basicConfig(
    level=logging.INFO, filename="Profile_updater.log", format="%(asctime)s    : %(message)s"
)
# logging.disable(logging.CRITICAL)
os.environ["WDM_LOCAL"] = "1"
os.environ["WDM_LOG_LEVEL"] = "0"


def log_msg(message):
    """Print to console and store to Log"""
    print(message)
    logging.info(message)


def catch(error):
    """Method to catch errors and log error details"""
    _, _, exc_tb = sys.exc_info()
    lineNo = str(exc_tb.tb_lineno)
    msg = "%s : %s at Line %s." % (type(error), error, lineNo)
    print(msg)
    logging.error(msg)


def getObj(locatorType):
    """This map defines how elements are identified"""
    map = {
        "ID": By.ID,
        "NAME": By.NAME,
        "XPATH": By.XPATH,
        "TAG": By.TAG_NAME,
        "CLASS": By.CLASS_NAME,
        "CSS": By.CSS_SELECTOR,
        "LINKTEXT": By.LINK_TEXT,
    }
    return map[locatorType.upper()]


def GetElement(driver, elementTag, locator="ID"):
    """Wait max 15 secs for element and then select when it is available"""
    try:

        def _get_element(_tag, _locator):
            _by = getObj(_locator)
            if is_element_present(driver, _by, _tag):
                return WebDriverWait(driver, 15).until(
                    lambda d: driver.find_element(_by, _tag)
                )

        element = _get_element(elementTag, locator.upper())
        if element:
            return element
        else:
            log_msg("Element not found with %s : %s" % (locator, elementTag))
            return None
    except Exception as e:
        catch(e)
    return None


def is_element_present(driver, how, what):
    """Returns True if element is present"""
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True


def WaitTillElementPresent(driver, elementTag, locator="ID", timeout=30):
    """Wait till element present. Default 30 seconds"""
    result = False
    driver.implicitly_wait(0)
    locator = locator.upper()

    for _ in range(timeout):
        time.sleep(0.99)
        try:
            if is_element_present(driver, getObj(locator), elementTag):
                result = True
                break
        except Exception as e:
            log_msg("Exception when WaitTillElementPresent : %s" % e)
            pass

    if not result:
        log_msg("Element not found with %s : %s" % (locator, elementTag))
    driver.implicitly_wait(3)
    return result


def tearDown(driver):
    try:
        driver.close()
        log_msg("Driver Closed Successfully")
    except Exception as e:
        catch(e)
        pass

    try:
        driver.quit()
        log_msg("Driver Quit Successfully")
    except Exception as e:
        catch(e)
        pass


def randomText():
    return "".join(choice(ascii_uppercase + digits) for _ in range(randint(1, 5)))


def LoadDriver(headless):
    """Open Chrome"""
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")  # ("--kiosk") for MAC
    options.add_argument("--disable-popups")
    options.add_argument("--disable-gpu")
    if headless:
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("headless")
        options.add_argument('--no-sandbox')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        
    # updated to use ChromeDriverManager to match correct chromedriver automatically
    driver = None
    try:
        driver = webdriver.Chrome(options, service=ChromeService(CM().install()))
    except:
        driver = webdriver.Chrome(options)
    log_msg("Google Chrome Launched!")

    driver.implicitly_wait(3)
    return driver


def UpdateResume():
    try:
        # random text with with random location and size
        config = load_config()
        originalResumePath = config.get("resume",{}).get("originalResumePath","")  
        modifiedResumePath = config.get("resume",{}).get("modifiedResumePath","")
        txt = randomText()
        xloc = randint(700, 1000)  # this ensures that text is 'out of page'
        fsize = randint(1, 10)

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont("Helvetica", fsize)
        can.drawString(xloc, 100, "lon")
        can.save()

        packet.seek(0)
        new_pdf = PdfReader(packet)
        existing_pdf = PdfReader(open(originalResumePath, "rb"))
        pagecount = len(existing_pdf.pages)
        print("Found %s pages in PDF" % pagecount)

        output = PdfWriter()
        # Merging new pdf with last page of my existing pdf
        # Updated to get last page for pdf files with varying page count
        for pageNum in range(pagecount - 1):
            output.add_page(existing_pdf.pages[pageNum])

        page = existing_pdf.pages[pagecount - 1]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        # save the new resume file
        with open(modifiedResumePath, "wb") as outputStream:
            output.write(outputStream)
        print("Saved modified PDF : %s" % modifiedResumePath)
        return os.path.abspath(modifiedResumePath)
    except Exception as e:
        catch(e)
    return os.path.abspath(originalResumePath)
