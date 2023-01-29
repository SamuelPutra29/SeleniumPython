# Conditional commands
from selenium import webdriver
#required for controlling browser By and Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#REQUIRED FOR HEADLESS PART 1
from selenium.webdriver.chrome.options import Options
#New paradigm for path - required
from selenium.webdriver.chrome.service import Service
import time

#print(time.time())

#Requirement #2 - Set your installed chrome driver.
# There is a video on this in the description
s = Service('/usr/local/bin/chromedriver')

#Set some selenium chrome options - Optional
#These options set your driver to run headless or not.
chromeOptions = Options()
chromeOptions.headless = False

#Initialize your Chrome Driver with services and options (optional)
#For mor info on running headless, there's a link below in description
driver = webdriver.Chrome(service=s, options=chromeOptions)


# This you have to run the driver here. Your execution will depend.
def starting_driver():
    driver.get("https://demo.nopcommerce.com")
    print("starting_Driver")
    driver.maximize_window() #maximize window
    time.sleep(1)
    
starting_driver()

# is_displayed & is_enabled
searchbox = driver.find_element(By.ID, 'small-searchterms')
print('Display status: ', searchbox.is_displayed())
print('Display status: ', searchbox.is_enabled())

# is_selected : To check the element already selected or not 

register = driver.find_element(By.LINK_TEXT,'Register').click()
male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print('Default radio buttons status....')
print('male button: ', male.is_selected())
print('female button: ', female.is_selected())

male.click()
print('After selecting male radio button...')
print('male button: ', male.is_selected())
print('female button: ', female.is_selected())










while True: 
    pass