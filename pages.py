from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import helpers
import data

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) # Initialize WebDriverWait

        # Addresses
        self.from_field = (By.ID, 'from')
        self.to_field = (By.ID, 'to')
        # Tariff and call button
        self.supportive_plan_card = (By.XPATH, '//div[contains(text(), "Supportive")]')
        self.supportive_plan_card_parent = (By.XPATH, '//div[contains(text(), "Supportive")]//..')
        self.active_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
        self.call_taxi_button = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
        # Phone number and code
        self.phone_number_field = (By.ID, 'phone')
        self.phone_code_field = (By.ID, 'code')
        # Credit Card
        self.card_number_field = (By.ID, 'cardNumber')
        self.card_code_field = (By.ID, 'code')
        self.link_card_button = (By.XPATH, '//button[contains(text(), "Link")]')
        # Driver comment
        self.driver_comment_field = (By.ID, 'comment')
        # Extras (blanket, handkerchiefs, ice cream)
        self.order_blanket_button = (By.ID, 'orderBlanket')
        self.blanket_ordered_check = (By.ID, 'blanketOrdered')
        self.order_handkerchiefs_button = (By.ID, 'orderHandkerchiefs')
        self.handkerchiefs_ordered_check = (By.ID, 'handkerchiefsOrdered')
        self.order_ice_cream_button = (By.ID, 'orderIceCream')
        self.ice_cream_count_element = (By.ID, 'iceCreamCount')
        # Car search modal
        self.car_search_modal = (By.ID, 'carSearchModal')

    def set_address(self, from_address, to_address):
        self.wait.until(expected_conditions.visibility_of_element_located(self.from_field)).clear()
        self.wait.until(expected_conditions.visibility_of_element_located(self.from_field)).send_keys(from_address)
        self.wait.until(expected_conditions.visibility_of_element_located(self.to_field)).clear()
        self.wait.until(expected_conditions.visibility_of_element_located(self.to_field)).send_keys(to_address)
        self.wait.until(expected_conditions.visibility_of_element_located(self.call_taxi_button))

    def select_supportive_plan(self):
        supportive_plan = self.wait.until(expected_conditions.element_to_be_clickable(self.supportive_plan_card))
        parent = self.driver.find_element(*self.supportive_plan_card_parent)
        active_plan = self.wait.until(expected_conditions.visibility_of_element_located(self.active_plan_card)).text
        if "Supportive" not in active_plan:
            supportive_plan.click()

    def fill_phone_number(self, phone_number):
        self.wait.until(expected_conditions.visibility_of_element_located(self.phone_number_field)).clear()
        self.wait.until(expected_conditions.visibility_of_element_located(self.phone_number_field)).send_keys(phone_number)
        phone_code = helpers.retrieve_phone_code()
        self.wait.until(expected_conditions.visibility_of_element_located(self.phone_code_field)).send_keys(phone_code)

    def add_credit_card(self, card_number, card_code):
        self.wait.until(expected_conditions.visibility_of_element_located(self.card_number_field)).send_keys(card_number)
        self.wait.until(expected_conditions.visibility_of_element_located(self.card_code_field)).send_keys(card_code)
        self.wait.until(expected_conditions.visibility_of_element_located(self.card_code_field)).send_keys(Keys.TAB)
        self.wait.until(expected_conditions.element_to_be_clickable(self.link_card_button)).click()

    def write_comment_for_driver(self, message):
        self.wait.until(expected_conditions.visibility_of_element_located(self.driver_comment_field)).clear()
        self.wait.until(expected_conditions.visibility_of_element_located(self.driver_comment_field)).send_keys(message)

    def order_blanket_and_handkerchiefs(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.order_blanket_button)).click()
        self.wait.until(expected_conditions.element_to_be_clickable(self.order_handkerchiefs_button)).click()

    def order_ice_creams(self, quantity=2):
        for _ in range(quantity):
            self.wait.until(expected_conditions.element_to_be_clickable(self.order_ice_cream_button)).click()

    def order_taxi(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.call_taxi_button)).click()

    def get_from(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.from_field)).get_attribute("value")

    def get_to(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.to_field)).get_attribute("value")

    def is_supportive_plan_selected(self):
        active_plan = self.wait.until(expected_conditions.visibility_of_element_located(self.active_plan_card)).text
        return "Supportive" in active_plan

    def get_phone_number(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.phone_number_field)).get_attribute("value")

    def get_driver_comment(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.driver_comment_field)).get_attribute("value")

    def is_blanket_ordered(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.blanket_ordered_check)).is_displayed()

    def is_handkerchiefs_ordered(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.handkerchiefs_ordered_check)).is_displayed()

    def get_ice_cream_count(self):
        return int(self.wait.until(expected_conditions.visibility_of_element_located(self.ice_cream_count_element)).text)

    def is_car_search_modal_visible(self):
        try:
            return self.wait.until(expected_conditions.visibility_of_element_located(self.car_search_modal)).is_displayed()
        except:
            return False
