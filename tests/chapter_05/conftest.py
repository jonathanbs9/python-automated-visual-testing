from os import close
import pytest
from applitools.selenium import Eyes
from selenium import webdriver

from config.base import APPLITOOLS_API_KEY

APP_NAME= 'automation_bookstore'
APP_UNDER_TEST= 'https://automationbookstore.dev/'

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(APP_UNDER_TEST)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def eyes():
    eyes = initialize_eyes()
    yield eyes

def initialize_eyes():
    eyes = Eyes()
    eyes.api_key = APPLITOOLS_API_KEY
    return eyes

def get_test_name():
    import inspect
    return inspect.stack()[3].function

def open_eyes(driver, eyes):
    eyes.open(driver, APP_NAME, test_name=get_test_name())

def close_eyes(eyes):
    eyes.close()

def validate_window(driver, eyes, tag=None):
    open_eyes(driver, eyes)
    #eyes.match_level=
    eyes.check_window(tag=tag)
    close_eyes(eyes)