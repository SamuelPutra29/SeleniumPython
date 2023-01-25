# This page is about Xpath Axes 
"""
self 
parent 
child
ancestor 
descendant 
following
following-sibling 
preceding 
preceding-sibling
"""
from StartDriver import * 

starting_driver()

# Self node
self_node = driver.find_element(By.XPATH,"//a[contains(text(),'Octal Credit Capital')]").text
print(self_node)

#parent
parent_node = driver.find_element(By.XPATH,"//a[contains(text(),'Octal Credit Capital')]/parent::td").text
print(parent_node)

# Child
child_node= driver.find_elements(By.XPATH,"//a[contains(text(),'Octal Credit Capital')]/ancestor::tr/child::td")
print(len(child_node))

# Anchestor 
Ancestor = driver.find_element(By.XPATH,"//a[contains(text(),'Octal Credit Capital')]/ancestor::tr").text
print(Ancestor)

# Descendant
Descendants =driver.find_elements(By.XPATH,"//a[contains(text(),'Octal Credit Capital')]/ancestor::tr/descendant::*")
print(len(Descendants))

# Following
following = driver.find_elements(By.XPATH,'//a[contains(text(),\'Octal Credit Capital\')]/ancestor::tr/following::*')
print('Number of following: ', len(following))


# Following sibling
following_sibling = driver.find_elements(By.XPATH,'//a[contains(text(),\'Octal Credit Capital\')]/ancestor::tr/following::*')
print('Number of following-sibling: ', len(following_sibling))

# Preceding 
preceding = driver.find_elements(By.XPATH,'//a[contains(text(),\'Octal Credit Capital\')]/ancestor::tr/preceding::*')
print('Number of preceding : ', len(preceding))

# Preceding-Sibling 
preceding_sibling = driver.find_elements(By.XPATH,'//a[contains(text(),\'Octal Credit Capital\')]/ancestor::tr/preceding::*')
print('Number of preceding-sibling : ', len(preceding_sibling))





while True: 
    pass