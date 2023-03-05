from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@then('Verify that Sign in page opened')
def verify_sign_in_page(context):
    expected_text = 'Sign in'
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'


@then('Verify that every product has a name and image')
def verify_products_name_tag(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)

    for product in all_products:
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Product image is missing'

        product_tile = product.find_element(*PRODUCT_TITLE).text
        assert product_tile, 'Product title is missing'


