from selenium.webdriver.common.by import By
from behave import given, when, then

#@given('Open Amazon page')
#def open_amazon(context):
    #context.driver.get('http://www.amazon.com/')

@when('Click on Returns and Orders')
def click_returns_and_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@then('Verify that Sign in page opened')
def verify_sign_in_page(context):
    expected_text = 'Sign in'
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'


