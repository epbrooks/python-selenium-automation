from selenium.webdriver.common.by import By
from behave import given, when, then


HEADER_LINKS = (By.CSS_SELECTOR, "div.celwidget.c-f div[class*='_p13n-zg-nav-tab-all_style_zg-tabs-li']")


@given('Open Amazon Bestsellers Page')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify Header links are present')
def verify_header_links(context):
    context.driver.find_elements(*HEADER_LINKS)


@then('Verify that header has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    expected_amount = int(5)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == (expected_amount), f'Expected {expected_amount} links but got {len(header_links)}'