#Test Case: Logged out user sees Sign in page when clicking Orders

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

service = Service('/Users/epbrooks/JobEasy/13-python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('http://wwww.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()

expected_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
print(actual_result)

assert expected_result == actual_result
print('Test case passed')

driver.quit()