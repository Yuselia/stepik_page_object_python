from selenium.webdriver.common.by import By



class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USERNAME_INPUT = (By.NAME, "login-username")
    LOGIN_PASSWORD_INPUT = (By.NAME, "login-password")
    LOGIN_SUBMIT_BUTTON = (By.NAME, "login_submit")

    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL_INPUT = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD1_INPUT = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2_INPUT = (By.NAME, "registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    MESSAGE_PRODUCT_WAS_ADDED = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")
    MESSAGE_WITH_BASKET_VALUE = (By.CLASS_NAME, "alert-info")




