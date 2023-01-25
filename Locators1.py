# Object Locators strategies using ID,NAME


from StartDriver import *
# Calling the function to start chrome driver 
starting_driver()


## These are the methods to find a single element: 

# 1. Using ID
#driver.find_element(By.ID,"small-searchterms").send_keys('Lenovo Thinkpad ')

# 2. Using Name 
#driver.find_element(By.NAME,"q").send_keys('Lenovo Thinkpad ')

# 3. Using LINKEDTEXT and PARTIALLINKEDTEXT
driver.find_element(By.LINK_TEXT,'Register').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Reg').click()


## These are the methods to find any elements 
# For finding more than one element, we can use ClassName and TagName 

driver.find_elements(By.CLASS_NAME,'class_name')
driver.find_elements(By.TAG_NAME,"")










# this syntax should be in the end of the code 
while (True):
    pass
