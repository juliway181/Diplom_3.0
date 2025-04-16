import allure

from constants import Constants
from locators.locators_lk import LkLocators
from pages.base_page import BasePage


class LkPage(BasePage):
    @allure.step("Нажать на кнопку 'История заказов'")
    def click_order_history(self):
        self.click_on_element(LkLocators.HISTORY_BUTTON)

    @allure.step("Нажать на кнопку 'Выход'")
    def click_exit_button(self):
        self.click_on_element(LkLocators.EXIT_BUTTON)

    @allure.step("Проверка url order history")
    def check_url_order_history(self):
        return self.check_url(Constants.URL_ORDER_HISTORY)

    @allure.step("Проверка url lk")
    def check_url_lk(self):
        return self.check_url(Constants.URL_LK)
