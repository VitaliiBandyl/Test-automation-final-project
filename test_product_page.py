from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.login_guest
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.add_to_basket_guest
class TestGuestAddToBasketFromProductPage:
    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.should_not_be_product()
        basket_page.should_be_message_empty_basket()

    @pytest.mark.parametrize('offer_number', ["0", "1", "2", "3", "4", "5", "6",
                                              pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
    def test_guest_can_add_product_to_basket(self, browser, offer_number):
        page = ProductPage(browser,
                           f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}")
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_added()

    @pytest.mark.xfail(reason="Negative test. Not to be fixed")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()


@pytest.mark.add_to_basket_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.should_not_be_product()
        basket_page.should_be_message_empty_basket()

    def test_user_cant_see_success_message(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser, setup):
        page = ProductPage(browser,
                           f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_added()


@pytest.mark.xfail(reason="Negative test. Not to be fixed")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_dissappear_of_success_message()
