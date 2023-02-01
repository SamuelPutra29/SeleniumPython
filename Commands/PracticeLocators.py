from StartDriver import *

starting_driver()

search_bar = driver.find_element(By.XPATH, '//*[@id=\'small-searchterms\']')
search_button = driver.find_element(
    By.XPATH, "//*[@id='small-searchterms']/following-sibling::button[text()='Search']")

search_bar.send_keys('Samsung')
search_button.click()


while True:
    pass
