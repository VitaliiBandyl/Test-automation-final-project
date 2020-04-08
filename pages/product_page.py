from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_item = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_item.click()
