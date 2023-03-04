from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep


#ADD_TO_CART_BTN =
#PRODUCT_NAME =
#PRODUCT_PRICE =
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
#CURRENT_COLOR =

@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com//dp/{product_id}/')


@then('Verify user can click through colors')
def verify_user_can_select_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click()

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)

    for color in all_color_options:
        color.click()
