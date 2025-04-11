import allure
from locators.locators_lk import LkLocators
from pages.base_page import BasePage


class LkPage(BasePage):
    @allure.step("Нажать на кнопку 'История заказов'")
    def click_order_history(self):
        self.click_on_element(LkLocators.HISTORY_BUTTON)

    @allure.step("Нажать на кнопку 'Выход'")
    def click_exit_button(self):
        self.click_on_element(LkLocators.EXIT_BUTTON)
