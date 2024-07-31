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

