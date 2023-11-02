from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()
        time.sleep(5)
        self.should_be_added_to_basket_alert()
        self.should_be_cost_of_basket_alert()

    def should_be_added_to_basket_alert(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_ALERT), "Added to basket alert is not presented"

    def should_be_cost_of_basket_alert(self):
        assert self.is_element_present(*ProductPageLocators.COST_OF_BASKET_ALERT), "Cost of basket alert is not presented"


