from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER = [By.XPATH, '//*[contains(@class, "OrderHistory_link")]']
    ORDER_STRUCTURE = [By.XPATH, '//p[text()="Cостав"]']
    ORDER_ID = [By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq"]
    CLOSE_MODAL_ORDER = [By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]"]
    ORDERS_AT_HISTORY = [By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                   "'text_type_digits-default')]"]
    ORDERS_AT_FEED = [By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                "text_type_digits-default']"]
    TOTAL_ORDER_COUNT = [By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"]
    DAILY_ORDER_COUNT = [By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"]
    NUMBER_ORDER_PROGRESS = [By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li']