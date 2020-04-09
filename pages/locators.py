from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group [href]")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
