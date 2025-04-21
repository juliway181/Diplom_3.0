from selenium.webdriver.common.by import By

class MainPageLocators:
    LK_BUTTON = By.XPATH, '//p[text()="Личный Кабинет"]'
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]/parent::a'
    LINE_ORDER_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'
    BUN_INGREDIENT = By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]'
    TEXT_WINDOW_INGR = By.XPATH, '//h2[text()="Детали ингредиента"]'
    CROSS_BUTTON = By.XPATH, '//button[contains(@class,"close")]'
    INGREDIENT_COUNTER = By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]'
    ORDER_BASKET = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDER_IDENTIFIER = By.XPATH, '//p[text()="идентификатор заказа"]'
    WAIT_WINDOW = By.XPATH, "//*[@alt='loading animation']/parent::div"
