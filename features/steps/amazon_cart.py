from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
EMPTY_CART = (By.CSS_SELECTOR, 'span#nav-cart-count')
SEARCH_WORD = (By.CSS_SELECTOR, 'input#twotabsearchtextbox')
CLICK_TABLET = (By.CSS_SELECTOR, "div[data-cel-widget='search_result_2'] span.a-size-medium")
CLICK_ADD_TO_CART = (By.CSS_SELECTOR, 'input#add-to-cart-button')
CLICK_NO_THANKS = (By.CSS_SELECTOR, 'span.abb-intl-decline')
CLICK_GO_TO_CART = (By.CSS_SELECTOR, "a[href='/gp/cart/view.html?ref_=sw_gtc']")
VERIFY_CART_ITEM = (By.CSS_SELECTOR, 'span#sc-subtotal-label-activecart')


@then('Verify that Amazon Cart is empty')
def verify_amazon_cart_empty(context):
    expected_text = '0'
    actual_text = context.driver.find_element(*EMPTY_CART).text
    assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}.'

@when('Input Tablets into search field')
def input_search_word(context):
    context.driver.find_element(*SEARCH_WORD).send_keys('tablets')


@when('Click on Amazon Fire HD 10 inch tablet')
def click_amazon_tablet(context):
    context.driver.find_element(*CLICK_TABLET).click()


@when('Click on Add to Cart')
def click_add_to_cart(context):
    context.driver.find_element(*CLICK_ADD_TO_CART).click()

@when('Click on No Thanks')
def click_no_thanks(context):
    context.driver.wait.until(EC.element_to_be_clickable(CLICK_NO_THANKS)).click()


@when('Click on Go to Cart')
def click_go_to_cart(context):
    context.driver.find_element(*CLICK_GO_TO_CART).click()


@then('Verify that Amazon Cart contains selected item')
def verify_cart_contains_item(context):
    expected_text = 'Subtotal (1 item):'
    actual_text = context.driver.find_element(*VERIFY_CART_ITEM).text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
