from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators


class TestLogout:
    def test_logout_from_personal_account(self,driver):
        login_into_account = driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON)
        login_into_account.click()

        wait = WebDriverWait(driver, 15)
#Входим
        email_input = driver.find_element(*Locators.AUTH_EMAIL_INPUT)  # Вводим email
        email_input.send_keys(Data.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.AUTH_PASSWORD_INPUT)  # Вводим пароль
        password_input.send_keys(Data.AUTH_PASSWORD)

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)  # Нажимаем на кнопку войти
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_all_elements_located(Locators.MAKE_ORDER_BUTTON))
#Переходим в персональный аккаунт
        login_into_personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        login_into_personal_account.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_all_elements_located(Locators.PROFILE_BUTTON))
#Выходим
        quit_from_account = driver.find_element(*Locators.LOGOUT_BUTTON)
        quit_from_account.click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_all_elements_located(Locators.LOGIN_BUTTON))
