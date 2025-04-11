import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_main_page import MainPageLocators
from pages.base_page import BasePage



class MainPage(BasePage):
    @allure.step("Клик на кнопку 'Личный кабинет'")
    def click_lk_button(self):
        self.click_on_element(MainPageLocators.LK_BUTTON)

    @allure.step("Клик на кнопку 'Лента Заказов'")
    def click_feed_orders_button(self):
        self.click_on_element(MainPageLocators.LINE_ORDER_BUTTON)

    @allure.step("Клик на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик на Булочку>")
    def click_bun_button(self):
        self.click_on_element(MainPageLocators.BUN_INGREDIENT)

    @allure.step("Клик на 'крестик' в деталях ингредиента")
    def click_cross_button(self):
        self.click_on_element(MainPageLocators.CROSS_BUTTON)

    @allure.step("Проверка окна с деталями ингредиента")
    def check_ingredient_details(self, text):
        ingredient = self.set_text_to_elemet(MainPageLocators.TEXT_WINDOW_INGR)
        return text == ingredient

    @allure.step('Получение значения счетчика ингредиентов')
    def get_counter_ingredient_by_index(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Проверить нахождение элемента на странице")
    def check_displayed_ingredient_details(self):
        check = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located
                                                     (MainPageLocators.TEXT_WINDOW_INGR))
        return check.is_displayed()

    @allure.step('Проверить невидимость элемента')
    def check_invisibility_ingredient_details(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element
                                                    (MainPageLocators.TEXT_WINDOW_INGR))


    @allure.step('Перетащить Булочку>')
    def add_filling_to_order(self):
        draggable = self.find_element_with_wait(MainPageLocators.BUN_INGREDIENT)
        droppable = self.find_element_with_wait(MainPageLocators.ORDER_BASKET)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_create_order_button(self):
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Проверка создания заказа')
    def check_create_order(self, text):
        issued = self.find_element_with_wait(MainPageLocators.ORDER_IDENTIFIER)
        return issued.text