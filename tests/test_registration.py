from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from helper import Help
from locators import Locators


class TestRegistration:
    def test_registration(self, driver):
        driver.get(Data.Stellar_reg_URL)

        name_input = driver.find_element(*Locators.NAME_INPUT) # Вводим имя
        name_input.send_keys(Data.REG_NAME)

        email_input = driver.find_element(*Locators.EMAIL_INPUT) # Вводим email
        email_input.send_keys(Help.generate_email())

        password_input = driver.find_element(*Locators.PASSWORD_INPUT) # Вводим пароль
        password_input.send_keys(Data.REG_PASSWORD)

        reg_button = driver.find_element(*Locators.REG_BUTTON) # Нажимаем на кнопку регистрации
        reg_button.click()

        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(Locators.LOGIN_BUTTON, Data.LOGIN_BUTTON))
        login_button = driver.find_element(*Locators.LOGIN_BUTTON)

        assert login_button.is_displayed(),"Кнопка 'Войти' не появилась после регистрации"


    def test_with_short_password(self,driver):
        driver.get(Data.Stellar_reg_URL)

        name_input = driver.find_element(*Locators.NAME_INPUT)  # Вводим имя
        name_input.send_keys(Data.REG_NAME)

        email_input = driver.find_element(*Locators.EMAIL_INPUT)  # Вводим email
        email_input.send_keys(Data.REG_EMAIL)

        short_password_input = driver.find_element(*Locators.PASSWORD_INPUT)  # Вводим короткий пароль
        short_password_input.send_keys(Data.SHORT_REG_PASSWORD)

        reg_button = driver.find_element(*Locators.REG_BUTTON)  # Нажимаем на кнопку регистрации
        reg_button.click()

        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(Locators.INVALID_PASSWORD, Data.INVALID_PASSWORD))
        invalid_password = driver.find_element(*Locators.INVALID_PASSWORD)

        assert invalid_password.is_displayed()










