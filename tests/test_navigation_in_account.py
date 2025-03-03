from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators


class TestNavigationInAccount:
        def login(self, driver):
            wait = WebDriverWait(driver, 15)

            login_into_account = driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON)
            login_into_account.click()

            email_input = driver.find_element(*Locators.AUTH_EMAIL_INPUT)  # Вводим email
            email_input.send_keys(Data.AUTH_EMAIL)

            password_input = driver.find_element(*Locators.AUTH_PASSWORD_INPUT)  # Вводим пароль
            password_input.send_keys(Data.AUTH_PASSWORD)

            login_button = driver.find_element(*Locators.LOGIN_BUTTON)  # Нажимаем на кнопку войти
            login_button.click()


        def test_navigation_to_personal_account(self,driver):
            self.login(driver)
            WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_all_elements_located(Locators.MAKE_ORDER_BUTTON))

            login_into_personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
            login_into_personal_account.click()

            WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_all_elements_located(Locators.PROFILE_BUTTON))

            profile_button = driver.find_element(*Locators.PROFILE_BUTTON)
            assert profile_button.is_displayed(), "Такой кнопки нет"

        def navigation_to_personal_account(self,driver):
            self.login(driver)
            WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_all_elements_located(Locators.MAKE_ORDER_BUTTON))

            login_into_personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
            login_into_personal_account.click()

            WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_all_elements_located(Locators.PROFILE_BUTTON))

            profile_button = driver.find_element(*Locators.PROFILE_BUTTON)
            assert profile_button.is_displayed(), "Такой кнопки нет"


        def test_navigation_from_personal_account_to_constructor(self,driver):
            self.navigation_to_personal_account(driver)
            constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
            constructor_button.click()

            WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_all_elements_located(Locators.MAKE_ORDER_BUTTON))
            make_order_button = driver.find_element(*Locators.MAKE_ORDER_BUTTON)
            assert make_order_button.is_displayed(), "Такой кнопки нет"

        def test_navigation_from_personal_account_to_stella_burgers(self,driver):
            self.navigation_to_personal_account(driver)
            stella_burgers_button = driver.find_element(*Locators.STELLA_BURGERS_BUTTON)
            stella_burgers_button.click()

            WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_all_elements_located(Locators.MAKE_ORDER_BUTTON))
            make_order_button = driver.find_element(*Locators.MAKE_ORDER_BUTTON)
            assert make_order_button.is_displayed(), "Такой кнопки нет"









