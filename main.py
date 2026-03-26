from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os


class WebAutomation:
    def __init__(self):

        # Define driver, options and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        download_path = os.getcwd() # cwd = current working directory
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)


        service = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options,service=service)

    def login(self, username,password):

        # Load the webpage
        self.driver.get("https://demoqa.com/login")

        # Locate username , password and login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')


        # Fill in username and password , and click login button
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)
        time.sleep(1)

    def fill_form(self, fullname,email, current_address, permanent_address):

        self.driver.get("https://demoqa.com/text-box")

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
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')
        time.sleep(1)

        # load info in form
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Locate Download element
        download = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7'))) # By.XPATH is also applicable
        download.click()

        # Download button
        download_file = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'downloadButton')))
        download_file.click()

        # { driver.execute_script } is used in selenium to prevent click ads
        # download_file = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'downloadButton')))
        # driver.execute_script("arguments[0].click();", download_file)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login("Nayanxyz", 'Nayanxyz@001')
    webautomation.fill_form("Nayan", "nayan@gmail.com", "Indore", "Indore")
    webautomation.download()
    webautomation.close()