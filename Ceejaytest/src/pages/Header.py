from Ceejaytest.src.SeleniumExtended import SeleniumExtended
#from Ceejaytest.src.pages.Locators.HeaderLocators import HeaderLocators

class Header():

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)