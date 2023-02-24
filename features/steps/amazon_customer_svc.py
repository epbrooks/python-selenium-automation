from selenium.webdriver.common.by import By
from behave import given, when, then


WELCOME_BANNER = (By.CSS_SELECTOR, 'h1.fs-heading.bolded')
WELCOME_QUICK_LINKS = (By.CSS_SELECTOR, 'div.issue-card-wrapper')
SEARCH_BANNER = (By.CSS_SELECTOR, 'label h2.fs-heading')
SEARCH_TEXT = (By.CSS_SELECTOR, 'input#hubHelpSearchInput')
HELP_TOPICS_BANNER = (By.XPATH, "//h2[text()='All help topics']")
HELP_QUICK_LINKS = (By.CSS_SELECTOR, 'li.help-topics')


@given('Open Amazon Customer Service page')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('Verify that Welcome Banner is present')
def verify_welcome_banner(context):
    expected_text = 'Welcome to Amazon Customer Service'
    actual_text = context.driver.find_element(*WELCOME_BANNER).text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

@then('Verify that {expected_links} welcome quick links are present')
def verify_welcome_links(context, expected_links):
    expected_links = int(expected_links)
    header_links = context.driver.find_elements(*WELCOME_QUICK_LINKS)
    assert len(header_links) == (expected_links), f'Expected {expected_links} links but got {len(header_links)}'

@then('Verify that Search banner is present')
def verify_search_banner(context):
    expected_text = 'Search our help library'
    actual_text = context.driver.find_element(*SEARCH_BANNER).text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'



@then('Verify that search text field is present')
def verify_search_text(context):
    expected_text = ''
    actual_text = context.driver.find_element(*SEARCH_TEXT).text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'


@then('Verify that All help topics banner is present')
def verify_help_banner(context):
    context.driver.find_element(*HELP_TOPICS_BANNER)
    expected_text = 'All help topics'
    actual_text = context.driver.find_element(*HELP_TOPICS_BANNER).text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

@then('Verify that {expected_links} help quick links are present')
def verify_help_links(context, expected_links):
    expected_links = int(expected_links)
    help_links = context.driver.find_elements(*HELP_QUICK_LINKS)
    assert len(help_links) == (expected_links), f'Expected {expected_links} links but got {len(help_links)}'