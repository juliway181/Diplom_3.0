import allure
from constants import Constants
from locators.locators_main_page import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Переход по клику на "Конструктор"')
    def test_go_to_constructor(self, driver):
        constructor = MainPage(driver)
        constructor.get_url(Constants.URL_LOGIN)
        constructor.click_constructor_button()
        assert driver.current_url == Constants.URL

    @allure.title('Переход по клику на "Лента Заказов"')
    def test_go_to_feed_orders(self, driver):
        feed = MainPage(driver)
        feed.get_url(Constants.URL_LOGIN)
        feed.click_feed_orders_button()
        assert driver.current_url == Constants.URL_FEED

    #
    @allure.title('Проверка открытия окна с деталями ингредиентов')
    def test_show_details_ingredients(self, driver):
        details = MainPage(driver)
        details.get_url(Constants.URL_LOGIN)
        details.click_constructor_button()
        details.click_bun_button()
        assert details.get_text_from_element(MainPageLocators.TEXT_WINDOW_INGR) == Constants.INGR_DETAILS

    @allure.title('Клик на крестик закрывает окно с деталями ингредиентов')
    def test_click_cross_exit_details_ingredients(self, driver):
        details = MainPage(driver)
        details.get_url(Constants.URL_LOGIN)
        details.click_constructor_button()
        details.click_bun_button()
        details.click_cross_button()
        details.check_invisibility_ingredient_details()
        assert details.check_displayed_ingredient_details() is False

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.')
    def test_counter_increased(self, driver):
        counter = MainPage(driver)
        counter.get_url(Constants.URL)
        pre_counter = counter.get_counter_ingredient_by_index()
        counter.add_filling_to_order()
        actual_counter = counter.get_counter_ingredient_by_index()
        assert pre_counter < actual_counter

    @allure.title('Залогиненный пользователь может оформить заказ.')
    def test_create_order_successful(self, driver):
        login = LoginPage(driver)
        login.get_url(Constants.URL_LOGIN)
        login.login("juliway181@mail.ru", "123456789")
        order = MainPage(driver)
        order.add_filling_to_order()
        order.click_create_order_button()
        assert order.get_text_from_element(MainPageLocators.ORDER_IDENTIFIER) == Constants.TEXT_CR_ORDER
