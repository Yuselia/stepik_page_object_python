from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_product_was_added_to_basket(self, product_name, price):
        self.should_be_correct_product_name_in_message(product_name)
        self.should_be_correct_price_in_message(price)

    def should_be_correct_product_name_in_message(self, product_name):
        assert product_name in self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_WAS_ADDED).text, f"There is no message with: {product_name}"

    def should_be_correct_price_in_message(self, price):
        assert price in self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_BASKET_VALUE).text, f"There is no message about basket value with price: {price}"






