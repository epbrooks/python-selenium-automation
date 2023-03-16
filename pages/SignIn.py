from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignIn(Page):
    SIGN_IN = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMPTY_CART = (By.CSS_SELECTOR, 'span#nav-cart-count')

    def verify_text(self, expected_text, *locator):
        self.verify_text(expected_text, *self.SIGN_IN)
