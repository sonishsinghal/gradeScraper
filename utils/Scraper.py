from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = '/DRIVERS/geckodriver'


def scraper(rollNumber:str=None, password:str=None)->str:
    if (rollNumber is None or password is None):
        raise KeyError("You must specify RollNumber and Password")
    try:
        driver = webdriver.Firefox(executable_path = DRIVER_PATH)
        driver.maximize_window()
        driver.delete_all_cookies()
        website='https://www.iitm.ac.in/viewgrades/'
        driver.get(website)
        username = driver.find_element_by_xpath('/html/body/div/div[1]/form/center/table[1]/tbody/tr[1]/td[2]/input')
        username.send_keys([rollNumber])
        password = driver.find_element_by_xpath('/html/body/div/div[1]/form/center/table[1]/tbody/tr[2]/td[2]/input')
        password.send_keys([password])
        submit= driver.find_element_by_xpath('/html/body/div/div[1]/form/center/table[2]/tbody/tr/td[1]/input')
        submit.click()
        driver.switch_to.frame(1)
        grade_html= driver.find_element_by_tag_name('html').get_attribute('innerHTML')
        return grade_html
    except:
        return 'Internal Server Error'