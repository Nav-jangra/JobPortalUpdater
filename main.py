import os

from utils.utils import LoadDriver
from utils.utils import log_msg,UpdateResume,tearDown,catch

from config.config import load_config
from core.foundit import founditLogin,UploadResume
from core.naukri import naukriLogin,naukriUploadResume,naukriUpdateProfile
from core.shine import shineLogin,shineUploadResume,shineUpdateProfile

def main():
    # Load configuration
    config = load_config()
    updateShine = config.get("updateProfiles").get("shine", False)
    updateFoundit = config.get("updateProfiles").get("foundIt", False)
    updateNaukri = config.get("updateProfiles").get("naukri", False)
    headless = config.get("headless")

    if(updateShine or updateNaukri or updateFoundit):
        log_msg("----Loading Browser -----\n")
        driver = LoadDriver(headless)
    
    try: 
        if driver:
            #updating resume 
            log_msg("\n----Reading Resume -----\n")
            originalResumePath = config.get("resume").get("originalResumePath", "")
            resumePath = originalResumePath
            if os.path.exists(originalResumePath):
                if config.get("updatePDF"):
                    log_msg("----Updating Resume -----\n")
                    resumePath = UpdateResume()
            else:
                log_msg("Resume not found at %s " % originalResumePath)

            #updating foundit profile
            if(updateFoundit):
                log_msg("\n----Updating foundit -----\n")
                status1,driver1 = founditLogin(driver)
                if(status1): 
                    UploadResume(driver1,resumePath)
                    log_msg("----FoundIt Update Succesful -----\n")

            
            #updating naukri Profile
            if(updateNaukri):
                log_msg("\n----Updating Naukri -----\n")
                statusNaukri, driverNaukri = naukriLogin(driver)
                if(statusNaukri): 
                    naukriUpdateProfile(driverNaukri)
                    naukriUploadResume(driverNaukri, resumePath)
                    log_msg("----Naukri Update Succesful -----\n")
            
            #updating shine Profile
            if(updateShine):
                log_msg("\n----Updating Shine -----\n")
                statusShine, driverShine = shineLogin(driver)
                if(statusShine): 
                    shineUpdateProfile(driverShine)
                    shineUploadResume(driverShine, resumePath) 
                    log_msg("----Shine Update Succesful -----\n")
 
        else:
            log_msg("Browser Loading failed")
    except Exception as e:
        catch(e)
    finally:
        tearDown(driver)

    log_msg("---- Script Run Ended-----\n")
    
if __name__ == "__main__":
    main()
