import data
import helpers
from pages import UrbanRoutesPage # Import the page class

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()  # Or your preferred browser
        cls.driver.implicitly_wait(10) # Adjust as needed
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def setup_method(self, method):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.routes_page = UrbanRoutesPage(self.driver)

    def test_set_route(self):
        self.routes_page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.routes_page.get_from() == data.ADDRESS_FROM
        assert self.routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.routes_page.select_supportive_plan()
        assert self.routes_page.is_supportive_plan_selected()

    def test_fill_phone_number(self):
        self.routes_page.fill_phone_number(data.PHONE_NUMBER)
        # Assuming there's a way to verify the phone number is filled correctly
        # For example, if there's a displayed phone number:
        assert self.routes_page.get_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.routes_page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        # Add assertions to verify card details, if possible
        # Example: assert self.routes_page.is_card_added()

    def test_comment_for_driver(self):
        self.routes_page.write_comment_for_driver(data.MESSAGE_FOR_DRIVER)
        assert self.routes_page.get_driver_comment() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.routes_page.order_blanket_and_handkerchiefs()
        assert self.routes_page.is_blanket_ordered()
        assert self.routes_page.is_handkerchiefs_ordered()

    def test_order_2_ice_creams(self):
        self.routes_page.order_ice_creams(2)
        assert self.routes_page.get_ice_cream_count() == 2

    def test_car_search_model_appears(self):
        self.routes_page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.routes_page.select_supportive_plan()
        self.routes_page.fill_phone_number(data.PHONE_NUMBER)
        self.routes_page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        self.routes_page.write_comment_for_driver(data.MESSAGE_FOR_DRIVER)
        self.routes_page.order_blanket_and_handkerchiefs()
        self.routes_page.order_ice_creams(2)
        self.routes_page.order_taxi()
        assert self.routes_page.is_car_search_modal_visible(), "Car search modal did not appear."
