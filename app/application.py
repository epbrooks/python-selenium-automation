from pages.header import Header
from pages.MainPage import MainPage
from pages.cart import Cart


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.MainPage = MainPage(self.driver)
        self.header = Header(self.driver)
        self.cart = Cart(self.driver)


