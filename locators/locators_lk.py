from selenium.webdriver.common.by import By

class LkLocators:
    HISTORY_BUTTON = [By.LINK_TEXT, 'История заказов']
    EXIT_BUTTON = [By.XPATH, ".//button[text()='Выход']"]