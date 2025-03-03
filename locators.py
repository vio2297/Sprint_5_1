from selenium.webdriver.common.by import By


class Locators:
    #Для регистрации
    NAME_INPUT = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::input")  # поле ввода имени
    EMAIL_INPUT = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")  # поле ввода почты
    PASSWORD_INPUT = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")  # поле ввода пароля
    REG_BUTTON = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # кнопка Зарегистрироваться
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']") #Кнопка войти
    INVALID_PASSWORD = (By.XPATH, ".//p[contains(text(),'Некорректный пароль')]") # сообщение об ошибке

    #Для авторизации
    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']") # кнопка оформить заказ
    AUTH_EMAIL_INPUT = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input") # для авторизации
    AUTH_PASSWORD_INPUT = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
    LOGIN_INTO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    REGISTRATION_FORM_LINK = (By.XPATH, ".//a[text() = 'Зарегистрироваться']") # ссылка на форму регистраии
    LOGIN_BUTTON_IN_REG_FORM = (By.XPATH, ".//a[text() = 'Войти']")

    RECOVER_PASSWORD_LINK = (By.XPATH, ".//a[text() = 'Восстановить пароль']")  # ссылка на форму восстановить пароль
    LOGIN_BUTTON_IN_FORG_PASSW_FORM = (By.XPATH, ".//a[text() = 'Войти']")

    # Навигация по личной аккаунту
    PROFILE_BUTTON = (By.XPATH, ".//a[text() = 'Профиль']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")
    STELLA_BURGERS_BUTTON = (By.XPATH, ".//*[@id='root']/div/header/nav/div")
    LOGOUT_BUTTON = (By.XPATH, " .//button[text() = 'Выход']")

    #Раздел конструктора
    SAUCES_SECTION = (By.XPATH, ".//span[text() = 'Соусы']")
    BUNS_SECTION = (By.XPATH, ".//span[text() = 'Булки']")
    FILLINGS_SECTION = (By.XPATH, ".//span[text() = 'Начинки']")



