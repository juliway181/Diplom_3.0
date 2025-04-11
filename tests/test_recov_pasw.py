import allure
from constants import Constants
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recov_pswd_page import PswdPage


class TestPersonalAcc:
    @allure.title('Проверка на переход по клику на "Восстановить" пароль на странице логина')
    def test_go_to_password_recovery_page_by_clicking_recover_password_link(self, driver):
        login_page = PswdPage(driver)
        login_page.get_url(Constants.URL_LOGIN)
        login_page.click_recovery_psw_button()
        assert driver.current_url == Constants.URL_FORGOT_PSW

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    def test_enter_email_and_click_recovery_button(self, driver):
        recovery_page = PswdPage(driver)
        recovery_page.get_url(Constants.URL_FORGOT_PSW)
        recovery_page.input_email_for_reset_password("xxx@mail.ru")
        recovery_page.click_recovery_button()
        assert driver.current_url == Constants.URL_FORGOT_PSW

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_on_show_password_button_activated_field(self, driver):
        recovery_page = PswdPage(driver)
        recovery_page.get_url(Constants.URL_FORGOT_PSW)
        recovery_page.input_email_for_reset_password("xxx@mail.ru")
        recovery_page.click_recovery_button()
        recovery_page.click_show_pswd()
        assert recovery_page.find_active_field()

