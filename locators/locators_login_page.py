from selenium.webdriver.common.by import By
class LogLocators:

    EMAIL_INPUT = [By.NAME, "name"]
    PSWD_INPUT = [By.NAME, "Пароль"]
    ENTER_BUTTON = [By.XPATH, "//*[text()='Войти']"]
    FORGOT_BUTTON = [By.XPATH, '//a[contains(@href, "/forgot-password")]']