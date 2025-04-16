import allure

from pages.lk_page import LkPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:
    @allure.title('Проверка отображения окна с данными о заказе')
    def test_open_order(self, driver):
        order = OrderPage(driver)
        order.go_feed_page()
        order.click_order()
        assert order.check_order_structure()

    @allure.title('Заказ пользователя из раздела «История заказов» отображается на странице «Лента заказов»')
    def test_id_order_history_found_in_feed_orders(self, driver):
        login = LoginPage(driver)
        login.go_login_page()
        login.login()
        create = MainPage(driver)
        create.add_filling_to_order()
        create.click_create_order_button()
        order = OrderPage(driver)
        order_id = order.get_order_id()
        order.click_cross_order()
        create.click_lk_button()
        account = LkPage(driver)
        account.click_order_history()
        id_order_history = order.order_id_found_history(order_id)
        create.click_feed_orders_button()
        id_order_feed = order.order_id_found_feed(order_id)
        assert id_order_history == id_order_feed

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается,')
    def test_total_counter_order(self, driver):
        login = LoginPage(driver)
        login.go_login_page()
        login.login()
        create = MainPage(driver)
        create.click_feed_orders_button()
        order = OrderPage(driver)
        counter_value = order.get_order_total_count()
        create.click_constructor_button()
        create.add_filling_to_order()
        create.click_create_order_button()
        order.wait_loading_cross_button()
        order.click_cross_order()
        create.click_feed_orders_button()
        counter_value_past = order.get_order_total_count()
        assert counter_value_past > counter_value

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_daily_counter_order(self, driver):
        login = LoginPage(driver)
        login.go_login_page()
        login.login()
        create = MainPage(driver)
        create.click_feed_orders_button()
        order = OrderPage(driver)
        counter_value = order.get_order_daily_count()
        create.click_constructor_button()
        create.add_filling_to_order()
        create.click_create_order_button()
        order.wait_loading_cross_button()
        order.click_cross_order()
        create.click_feed_orders_button()
        counter_value_past = order.get_order_daily_count()
        assert counter_value_past > counter_value

    @allure.title('После оформления заказа его номер появляется в разделе в работе')
    def test_new_order_show_work_list(self, driver):
        login = LoginPage(driver)
        login.go_login_page()
        login.login()
        create = MainPage(driver)
        create.add_filling_to_order()
        create.click_create_order_button()
        order = OrderPage(driver)
        order_id = order.get_order_id()
        order.click_cross_order()
        create.click_feed_orders_button()
        number = order.get_user_order_number(order_id)
        order_in_work = order.get_user_order_in_progress()
        assert order_in_work == number
