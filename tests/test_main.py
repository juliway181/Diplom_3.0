import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Переход по клику на "Конструктор"')
    def test_go_to_constructor(self, driver):
        constructor = MainPage(driver)
        login = LoginPage(driver)
        login.go_login_page()
        constructor.click_constructor_button()
        assert constructor.check_url_main()

    @allure.title('Переход по клику на "Лента Заказов"')
    def test_go_to_feed_orders(self, driver):
        feed = MainPage(driver)
        feed.go_main_page()
        feed.click_feed_orders_button()
        assert feed.check_url_feed()

    #
    @allure.title('Проверка открытия окна с деталями ингредиентов')
    def test_show_details_ingredients(self, driver):
        details = MainPage(driver)
        details.go_main_page()
        details.click_constructor_button()
        details.click_bun_button()
        assert details.check_ingredient_details()

    @allure.title('Клик на крестик закрывает окно с деталями ингредиентов')
    def test_click_cross_exit_details_ingredients(self, driver):
        details = MainPage(driver)
        details.go_main_page()
        details.click_constructor_button()
        details.click_bun_button()
        details.click_cross_button()
        details.check_invisibility_ingredient_details()
        assert details.check_displayed_ingredient_details() is False

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.')
    def test_counter_increased(self, driver):
        counter = MainPage(driver)
        counter.go_main_page()
        pre_counter = counter.get_counter_ingredient_by_index()
        counter.add_filling_to_order()
        actual_counter = counter.get_counter_ingredient_by_index()
        assert pre_counter < actual_counter

    @allure.title('Залогиненный пользователь может оформить заказ.')
    def test_create_order_successful(self, driver):
        login = LoginPage(driver)
        login.go_login_page()
        login.login()
        order = MainPage(driver)
        order.add_filling_to_order()
        order.click_create_order_button()
        assert order.check_order()
