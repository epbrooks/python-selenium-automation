from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('http://www.amazon.com/')

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon')

@then('Verify that Amazon Cart is empty')
def verify_amazon_cart_empty(context):
    expected_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}.'


