from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver,options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options,service=service)

# load the webpage
driver.get("https://demoqa.com/login")

# locate username, password and login buttons
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Fill in username and password, and click the button
username_field.send_keys('Nayanxyz')
password_field.send_keys('Nayanxyz@001')
driver.execute_script("arguments[0].click();", login_button)

input("press enter to close the browser")
driver.quit()