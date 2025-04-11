import allure
from constants import Constants
from pages.lk_page import LkPage
from pages.login_page import LoginPage
from pages.main_page import MainPage




class TestLk:
    @allure.title('Переход по клику на "Личный кабинет"')
    def test_go_to_personal_account(self, driver):
        login = LoginPage(driver)
        login.get_url(Constants.URL_LOGIN)
        login.login("juliway181@mail.ru", "123456789")
        main_page = MainPage(driver)
        main_page.click_lk_button()
        assert driver.current_url == Constants.URL_ACC

    @allure.title('Переход в раздел "История заказов"')
    def test_go_to_feed_orders(self, driver):
        login = LoginPage(driver)
        login.get_url(Constants.URL_LOGIN)
        login.login("juliway181@mail.ru", "123456789")
        main_page = MainPage(driver)
        main_page.click_lk_button()
        lk_page = LkPage(driver)
        lk_page.click_order_history()
        assert driver.current_url == Constants.URL_ORDER_HISTORY

    @allure.title('Выход из аккаунта')
    def test_logout_from_account(self, driver):
        login = LoginPage(driver)
        login.get_url(Constants.URL_LOGIN)
        login.login("juliway181@mail.ru", "123456789")
        main_page = MainPage(driver)
        main_page.click_lk_button()
        lk_page = LkPage(driver)
        lk_page.click_exit_button()
        assert driver.current_url == Constants.URL_LK
