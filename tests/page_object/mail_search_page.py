from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class MailSearchPage(BasePage):

    # Riddle of Stones
    @property
    def search_input(self):
        locator = Locator(By.ID, 'q')
        return BaseElement(self.driver,  locator=locator)

    @property
    def search_input_result(self):
        locator = Locator(By.NAME, 'q')
        return BaseElement(self.driver,  locator=locator)

    @property
    def search_button(self):
        locator = Locator(By.ID, 'search:submit')
        return BaseElement(self.driver,  locator=locator)

