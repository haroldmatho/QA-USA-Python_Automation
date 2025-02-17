from selenium import webdriver
from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators (we'll add more as we progress)
        self.address_from = (By.ID, "address-from")
        self.address_to = (By.ID, "address-to")
        # ... (more locators to be added)

    # Methods (we'll add more as we progress)
    def set_address(self, from_address, to_address):
        self.driver.find_element(*self.address_from).send_keys(from_address)
        self.driver.find_element(*self.address_to).send_keys(to_address)

    def select_supportive_plan(self):
        # Assuming 'Supportive' plan has a specific ID or class
        supportive_plan = self.driver.find_element(By.ID, "supportive-plan")
        if supportive_plan:  # Check if the element is found
            supportive_plan.click()

    def fill_phone_number(self, phone_number):
        phone_field = self.driver.find_element(By.ID, "phone-number")
        phone_field.send_keys(phone_number)

    def add_credit_card(self, card_number, card_code):
        # ... (implementation for adding a credit card)
        pass  # Placeholder for now

    def write_comment_for_driver(self, message):
        comment_field = self.driver.find_element(By.ID, "driver-comment")
        comment_field.send_keys(message)

    def order_blanket_and_handkerchiefs(self):
        # ... (implementation for ordering items)
        pass  # Placeholder for now

    def order_ice_creams(self, quantity=2):
        for _ in range(quantity):
            # ... (implementation for ordering ice cream)
            pass  # Placeholder for now

    def order_taxi(self):
        order_button = self.driver.find_element(By.ID, "order-taxi")
        order_button.click()

    def is_car_search_modal_visible(self):
        # ... (check if the car search modal is visible)
        pass  # Placeholder for now