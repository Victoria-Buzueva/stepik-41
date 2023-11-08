from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def guest_see_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "The guest doesn't see the message about an empty basket"

    def guest_has_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_PRODUCT), "The guest hasn't products in the basket"

    def guest_has_not_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), "The guest has products in the basket"


