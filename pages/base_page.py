import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Старт Драйвер")
    def get_url(self, URL):
        self.driver.get(URL)

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Проверить нахождение элемента в DOM-дереве страницы")
    def check_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step("Проверить нахождение  хотя бы одного элемента на странице")
    def check_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Проверить невидимость элемента")
    def check_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    @allure.step("Найти элемент с ожиданием")
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step("Нажать на элемент")
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step("Получить текст с элемента")
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step("Проверка присутствия текста в элементе")
    def check_text_in_element(self, locator, text):
        return WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Установить текст")
    def set_text_to_elemet(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step("Проверка URL")
    def check_url(self, url):
        element = self.driver.current_url
        return element == url

    @allure.step("Проверка текста в элементе")
    def check_texts(self, locator, text):
        return self.get_text_from_element(locator) == text
