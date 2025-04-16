from selenium.webdriver.common.by import By

class ResetPswdLocators:
    INPUT_EMAIL = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
    BUTTON_RESET = [By.XPATH, '//button[text()="Восстановить"]']
    BUTTON_RECOVERY = [By.LINK_TEXT, "Восстановить пароль"]
    BUTTON_SHOW = [By.XPATH, "//*[contains(@class, 'input__icon')]"]
    ACTIVE_FILED = [By.CSS_SELECTOR, '.input.input_status_active']