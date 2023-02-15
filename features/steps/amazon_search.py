from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('http://www.amazon.com/')

@when('Click on Returns and Orders')
def click_returns_and_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@then('Verify that Sign in page opened')
def verify_sign_in_page(context):
    expected_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}.'

