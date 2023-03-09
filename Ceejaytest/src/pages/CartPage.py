from Ceejaytest.src.SeleniumExtended import SeleniumExtended
from Ceejaytest.src.pages.Locators.CartPageLocators import CartPageLocators


class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cart_page(self):
        pass