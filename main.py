import data
import helpers
from pages import UrbanRoutesPage # Import the page class

class TestUrbanRoutes:
    # ... (setup_class and teardown_class remain the same)

    def test_set_route(self):
        page = UrbanRoutesPage(self.driver)
        page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_select_plan(self):
        page = UrbanRoutesPage(self.driver)
        page.select_supportive_plan()

    def test_fill_phone_number(self):
        page = UrbanRoutesPage(self.driver)
        page.fill_phone_number(data.PHONE_NUMBER)

    def test_fill_card(self):
        page = UrbanRoutesPage(self.driver)
        page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)

    def test_comment_for_driver(self):
        page = UrbanRoutesPage(self.driver)
        page.write_comment_for_driver(data.MESSAGE_FOR_DRIVER)

    def test_order_blanket_and_handkerchiefs(self):
        page = UrbanRoutesPage(self.driver)
        page.order_blanket_and_handkerchiefs()

    def test_order_2_ice_creams(self):
        page = UrbanRoutesPage(self.driver)
        page.order_ice_creams(2) # Moved the loop here

    def test_car_search_model_appears(self):
        page = UrbanRoutesPage(self.driver)
        page.order_taxi()
        assert page.is_car_search_modal_visible(), "Car search modal did not appear."