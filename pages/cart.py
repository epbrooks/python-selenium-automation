from selenium.webdriver.common.by import By
from pages.base_page import Page

class Cart(Page):
    EMPTY_CART = (By.CSS_SELECTOR, 'span#nav-cart-count')

    def verify_amazon_cart_empty(self, expected_text, *locator):
        self.verify_amazon_cart_empty(expected_text, *self.EMPTY_CART)

