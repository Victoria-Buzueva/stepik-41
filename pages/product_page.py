from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
        # self.solve_quiz_and_get_code()
        # time.sleep(5)
        self.should_be_added_to_basket_alert()
        self.should_be_cost_of_basket_alert()

    def should_be_added_to_basket_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Added to basket alert is not presented"
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        messages = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        assert name.text == messages[0].text, \
            f"The product name does not match: {name.text} - {messages[0].text}"

    def should_be_cost_of_basket_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Cost of basket alert is not presented"
        messages = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert price.text == messages[2].text, \
            f"The price of the product does not match: {price.text} - {messages[2].text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
           "Success message is presented, but should not be"

    def should_be_dissapeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message is not disappeared"

