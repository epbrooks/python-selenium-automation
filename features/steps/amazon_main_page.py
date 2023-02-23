from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
AMAZON_CART_ICON = (By.CSS_SELECTOR, 'span.nav-cart-icon')
AMAZON_SUBMIT = (By.CSS_SELECTOR, 'input#nav-search-submit-button')
AMAZON_RETURNS = (By.ID, 'nav-orders')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('http://www.amazon.com/')

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*AMAZON_CART_ICON).click()


@when('Clicks on search icon')
def click_search(context):
    context.driver.find_element(*AMAZON_SUBMIT).click()
    #context.driver.find_element(By.ID, "nav-search-submit-button")


@when('Click on Returns and Orders')
def click_returns_and_orders(context):
    context.driver.find_element(*AMAZON_RETURNS).click()