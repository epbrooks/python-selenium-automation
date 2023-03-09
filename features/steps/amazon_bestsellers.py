from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


HEADER_LINKS = (By.CSS_SELECTOR, "div.celwidget.c-f div[class*='_p13n-zg-nav-tab-all_style_zg-tabs-li']")
CURRENT_LINK = (By.CSS_SELECTOR, "div.celwidget.c-f div[class*='_p13n-zg-nav-tab-all_style_zg-tabs-li'] a[href]")

@given('Open Amazon Bestsellers Page')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify Header links are present')
def verify_header_links(context):
    context.driver.find_elements(*HEADER_LINKS)


@then('Verify that header has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == (expected_amount), f'Expected {expected_amount} links but got {len(header_links)}'


@then('Click on each link and verify that correct page opens')
def click_and_verify_header_links(context):


    all_header_links = context.driver.find_elements(*HEADER_LINKS)
    print('All header links: ', all_header_links)
    expected_links = ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']

    actual_links = []
    for i in range(len(expected_links)):
        link = context.driver.find_elements(*CURRENT_LINK)[i]
        link.click()
        current_link = context.driver.find_elements(*CURRENT_LINK)[i].text
        actual_links += [current_link]

    assert expected_links == actual_links, f'Expected {expected_links}, but got {actual_links}'