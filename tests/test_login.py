from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators


class TestUserLogin:

    def login(self,driver):

        wait = WebDriverWait(driver, 15)

        email_input = driver.find_element(*Locators.AUTH_EMAIL_INPUT)  # Вводим email
        email_input.send_keys(Data.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.AUTH_PASSWORD_INPUT)  # Вводим пароль
        password_input.send_keys(Data.AUTH_PASSWORD)

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)  # Нажимаем на кнопку войти
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.presence_of_all_elements_located(Locators.MAKE_ORDER_BUTTON))


    def test_login_through_login_to_account_button(self, driver):

        login_into_account = driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON)
        login_into_account.click()

        self.login(driver)

        make_order_button = driver.find_element(*Locators.MAKE_ORDER_BUTTON)

        assert make_order_button.is_displayed(), 'Кнопки оформить заказ нет'

    def test_login_through_personal_account_button(self, driver):

        login_into_personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        login_into_personal_account.click()

        self.login(driver)

        make_order_button = driver.find_element(*Locators.MAKE_ORDER_BUTTON)
        assert make_order_button.is_displayed(), 'Кнопки оформить заказ нет'

    def test_login_through_registration_button(self,driver):

        login_into_account = driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON)
        login_into_account.click()

        registration_button = driver.find_element(*Locators.REGISTRATION_FORM_LINK)
        registration_button.click()

        login_link_in_reg_button = driver.find_element(*Locators.LOGIN_BUTTON_IN_REG_FORM)
        login_link_in_reg_button.click()

        self.login(driver)

        make_order_button = driver.find_element(*Locators.MAKE_ORDER_BUTTON)
        assert make_order_button.is_displayed(), 'Кнопки оформить заказ нет'


    def test_login_through_password_recovery_button(self,driver):

        login_into_account = driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON)
        login_into_account.click()

        recovery_button = driver.find_element(*Locators.RECOVER_PASSWORD_LINK)
        recovery_button.click()

        login_link_in_rec_pass = driver.find_element(*Locators.LOGIN_BUTTON_IN_FORG_PASSW_FORM)
        login_link_in_rec_pass.click()

        self.login(driver)
        make_order_button = driver.find_element(*Locators.MAKE_ORDER_BUTTON)
        assert make_order_button.is_displayed(), 'Кнопки оформить заказ нет'




















