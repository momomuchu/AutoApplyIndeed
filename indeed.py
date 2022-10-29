from distutils.log import Log
import sys
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        

import time
from time import sleep
from config import *
from selenium.webdriver.chrome.options import Options


cache=[]
research="python"
login_url='https://secure.indeed.com/auth?hl=fr_FR&co=FR&continue=https%3A%2F%2Ffr.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Ffr.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess'
account_email = 'mohamedmaache68@gmail.com'  # your indeed email
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH,xpath)
    except NoSuchElementException:
        return False
    return True
def cookie():
    driver.find_element(By.ID,f'onetrust-accept-btn-handler').click()

def Login():
    driver.get(login_url)
    WebDriverWait(driver, 360).until(lambda x: x.find_element(By.CLASS_NAME, "icl-TextInput"))
    print('login success')
    driver.find_element(By.ID,"text-input-what").send_keys(research)
    driver.find_element(By.CLASS_NAME,"yosegi-InlineWhatWhere-primaryButton").send_keys(Keys.ENTER)

def Apply():
    while 'apply.indeed' in driver.current_url:
        if 'post-apply' in driver.current_url:
            driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[1]/main/div[4]/button')
        else:
            driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button')
        


def Apply_All():
    job_page=driver.find_elements(By.CLASS_NAME,"slider_container.css-g7s71f.eu4oa1w0")
    for i in range(len(job_page)):
        time.sleep(5)
        job_page[i].click()
        sleep(3)    
        print('keoef')
        if check_exists_by_xpath('/html/body/main/div/div[1]/div/div/div[5]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[3]/div/div[2]/div/div/span/div[2]/button/div/span[contains(text(),"simpl")]'):
            print('dsd')
            driver.find_element(By.CLASS_NAME,f'css-zv0ejl.e8ju0x51').send_keys(Keys.ENTER)

            driver.find_element(By.CLASS_NAME,'css-zv0ejl.e8ju0x51').click()
            window=driver.window_handles
            print(window)
            driver.switch_to(window[0])
            sleep(2)
            driver.close()
            sleep(5)
            driver.find_element(By.XPATH,f'/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button').send_keys(Keys.ENTER)
            sleep(2)
            driver.find_element(By.XPATH,f'/html/body/div[3]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button').send_keys(Keys.ENTER)
            sleep(2)
            driver.find_element(By.XPATH,f'//*[@id="ia-container"]/div/div/div/main/div[2]/div[2]/div/div/div[2]/div').send_keys(Keys.ENTER)
            sleep(2)

            driver.find_element(By.XPATH,'//*[@id="returnToSearchButton"]').send_keys(Keys.ENTER)
def NextPage():
    driver.find_element(By.XPATH,'//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[6]/a').send_keys(Keys.ENTER)

def ChangeCountry(encoder_name):
    driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/footer/div/ul[1]/li[8]/a').send_keys(Keys.ENTER)
    driver.find_element(By.XPATH,f'//a[@data-country-code={encoder_name}]').send_keys(Keys.ENTER)

def End_Apply():
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button').send_keys(Keys.ENTER)



Login()
job_page=driver.find_elements(By.CLASS_NAME,"slider_container.css-g7s71f.eu4oa1w0")
for i in range(len(job_page)):
    sleep(5)
    job_page[i].click()
    sleep(3)

    driver.find_element(By.CLASS_NAME,'css-zv0ejl.e8ju0x51').click()
    window=driver.window_handles
    print(window)
    driver.switch_to(window[0])
    Apply()

    
NextPage()

# to apply class=jobsearch-ViewJobContainer-inner
time.sleep(1000)