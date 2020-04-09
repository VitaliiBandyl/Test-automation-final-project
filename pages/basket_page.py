from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket url is not opened"

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Some product in basket"

    def should_be_message_empty_basket(self):
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
        assert "Your basket is empty." in message, "Empty basket message is not present"
