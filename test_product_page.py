from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()

    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    print("\nProduct: ", product_name, ", price: ", product_price)

    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_product_was_added_to_basket(product_name, product_price)






