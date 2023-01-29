# Xpath Options: 
"""
and 
or 
contains()
starts-with()
text()
"""
# How to write relative xpath 
# //tagname[@attribute='value']
# //*[@id='value']

# We can also use some methods 
# contains, starts-with 
# syntax -> //*[contains(@attribute,'value')]
#            //*[starts-with(@attribute,'value')]
#            //*[text()='value']




from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Commands.StartDriver import *
# Calling the function to start chrome driver 
#starting_driver()

#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="u_0_e_Im"]'))).click()







#while True:
 #   pass