from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class GoogleSearchPage(BasePage):

    # Riddle of Stones
    @property
    def search_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="q"]')
        return BaseElement(self.driver,  locator=locator)

    @property
    def search_button(self):
        locator = Locator(By.CSS_SELECTOR, 'input[name="btnK"]')
        return BaseElement(self.driver,  locator=locator)

