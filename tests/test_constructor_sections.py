from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators


class TestConstructorSection:
    def login_in(self,driver):
        login_into_account = driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON)
        login_into_account.click()

        wait = WebDriverWait(driver, 15)
        # Входим
        email_input = driver.find_element(*Locators.AUTH_EMAIL_INPUT)  # Вводим email
        email_input.send_keys(Data.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.AUTH_PASSWORD_INPUT)  # Вводим пароль
        password_input.send_keys(Data.AUTH_PASSWORD)

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)  # Нажимаем на кнопку войти
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_all_elements_located(Locators.MAKE_ORDER_BUTTON))

    def test_constructor_sauces_section(self,driver):
        self.login_in(driver)
        sauces_section = driver.find_element(*Locators.SAUCES_SECTION)
        sauces_section.click()
        assert sauces_section.is_displayed(), "Такой секции нет"

    def test_constructor_buns_section(self,driver):
        self.login_in(driver)
        sauces_section = driver.find_element(*Locators.SAUCES_SECTION)
        sauces_section.click()
        assert sauces_section.is_displayed()

        buns_section = driver.find_element(*Locators.BUNS_SECTION)
        buns_section.click()
        assert buns_section.is_displayed(), "Такой секции нет"


    def test_constructor_fillings_section(self,driver):
        self.login_in(driver)
        sauces_section = driver.find_element(*Locators.SAUCES_SECTION)
        sauces_section.click()
        assert sauces_section.is_displayed()

        fillings_section = driver.find_element(*Locators.FILLINGS_SECTION)
        fillings_section.click()
        assert  fillings_section.is_displayed(), "Такой секции нет"



