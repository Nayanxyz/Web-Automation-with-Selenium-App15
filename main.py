from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Define driver, options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options,service=service)

# Load the webpage
driver.get("https://demoqa.com/login")

# Locate username , password and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')


# Fill in username and password , and click login button
username_field.send_keys('Nayanxyz')
password_field.send_keys('Nayanxyz@001')
driver.execute_script("arguments[0].click();", login_button)
time.sleep(1)

driver.get("https://demoqa.com/text-box")

# DEMOQA website has too many ads, The below code works , but the probability of crashing is high, it is hard for selenium to locate elements,
# but another method is to ByPass two steps and land on the fields directly .

            # Locate the elements breakdown and textbox
            # elements = (WebDriverWait(driver, 10)
            #             .until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div/div[1]/span'))))
            # elements.click()
            # time.sleep(2)

            # text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
            # driver.execute_script("arguments[0].scrollIntoView({block : 'center'});", text_box)
            # time.sleep(1)
            # driver.execute_script("arguments[0].click();", text_box)
            # time.sleep(5)

# Locate form fields and submit button
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')
time.sleep(1)

# load info in form
fullname_field.send_keys('Nayan')
email_field.send_keys('nayan@gmail.com')
current_address_field.send_keys('indore')
permanent_address_field.send_keys('indore')
driver.execute_script("arguments[0].click();", submit_button)




input("press enter to close the browser")
driver.quit()