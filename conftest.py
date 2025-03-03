import pytest
from selenium import webdriver

from data import Data
from locators import Locators


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get(Data.Stellar_URL)
    
    yield chrome_driver

    chrome_driver.quit()
