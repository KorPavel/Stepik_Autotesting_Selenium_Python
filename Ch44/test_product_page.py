import pytest
from .pages.product_page import ProductPage

params = [x if x != 7 else pytest.param(x, marks=pytest.mark.xfail) for x in range(10)]

@pytest.mark.parametrize('param', params)
def test_guest_can_add_product_to_basket(browser, param):

    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{param}'

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()