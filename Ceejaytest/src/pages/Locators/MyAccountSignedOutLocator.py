# from selenium.webdriver.common.by import By
#
# class MyAccountSignedOutLocator:
#
#     LOGIN_USER_NAME = (By.ID, "username")
#     LOGIN_PASSWORD = (By.ID, "password")
#     LOGIN_BTN = (By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
#
#     ERRORS_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')


from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:

    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[value="Log in"]')

    ERRORS_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')

    # REGISTER ACCOUNT

    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[value="Register"]')




