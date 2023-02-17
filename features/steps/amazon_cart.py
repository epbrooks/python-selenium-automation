from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('http://www.amazon.com/')

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon')

@then('Verify that Amazon Cart is empty')
def verify_amazon_cart_empty(context):
    expected_result = context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon')
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon')
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}.'

@when('Input Tablets into search field')
def input_search_word(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox').send_keys('tablets')

@when('Clicks on search icon')
def click_search(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input#nav-search-submit-button')


@when('Click on Amazon Fire HD 10 inch tablet')
def click_amazon_tablet(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-cel-widget='search_result_2'] span.a-size-medium")


@when('Click on Add to Cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input#add-to-cart-button')


@when('Click on Go to Cart')
def click_go_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/cart/view.html?ref_=sw_gtc']")


@then('Verify that Amazon Cart contains selected item')
def verify_cart_contains_item(context):
    expected_result = context.driver.find_element(By.CSS_SELECTOR, 'span#sc-subtotal-label-activecart')
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span#sc-subtotal-label-activecart')
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}.'
