from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    AMAZON_RETURNS = (By.ID, 'nav-orders')
    AMAZON_CART_ICON = (By.CSS_SELECTOR, 'span.nav-cart-icon')

    def click_returns_and_orders(self):
        self.click(*self.AMAZON_RETURNS)

    def click_cart(self):
        self.click(*self.AMAZON_CART_ICON)

