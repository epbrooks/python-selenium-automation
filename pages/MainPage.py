from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    def open_url(self, url):
        self.open_url('https://www.amazon.com/')
