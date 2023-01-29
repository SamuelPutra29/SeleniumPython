from StartDriver import *

starting_driver()

# We will discuss about CSS selector 
#   1. Tag and ID
#   2. Tag and Class
#   3. Tag and attribute
#   4. Tag, class and attribute

# First Combination: tagname and ID
# driver.find_element(By.CSS_SELECTOR,'input#email') -> tagname#ID

# Second Combination: tagname and class 
# driver.find_element(By.CSS_SELECTOR,'input.inputtext_55_23')-> tagname.class

# Third Combination 
# driver.find_element(By.CSS_SELECTOR,'input[data-testid=royal_email])-> tagname[attribute=value]

# Fourth combination
# driver.find_element(By.CSS_SELECTOR,'tagname.valueofclass[attribute=value])





while True:
    pass