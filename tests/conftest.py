import pytest
import time
from variables import *
from pom.BasePage.basemodel import Basemodel
from src.locators.builder import Elements

# """Переход на страницу Формы из меню навигации"""


@pytest.fixture(scope="function")
def forms_page(browser):
    Basemodel(browser).find_by("xpath", Elements(browser).page_link_on_navigation_menu(forms)).click()
    time.sleep(2)
    return browser


@pytest.fixture(scope="function")
def quiz_page(browser):
    Basemodel(browser).find_by("xpath", Elements(browser).page_link_on_navigation_menu(quiz)).click()
    time.sleep(2)
    return browser


@pytest.fixture(scope="function")
def video_page(browser):
    Basemodel(browser).find_by("xpath", Elements(browser).page_link_on_navigation_menu(video)).click()
    time.sleep(2)
    return browser


"""Переход на страницу Возможности"""


@pytest.fixture(scope="function")
def forms_feature_page(browser):
    Basemodel(browser).find_by("xpath", Elements(browser).page_link_on_navigation_menu(forms)).click()
    time.sleep(2)
    Basemodel(browser).find_by("xpath", Elements(browser).page_link_on_navigation_menu(features)).click()
    time.sleep(2)
    return browser


@pytest.fixture(scope="function")
def quiz_feature_page(browser):
    Basemodel(browser).find_by("xpath", Elements(browser).page_link_on_navigation_menu(quiz)).click()
    time.sleep(2)
    Basemodel(browser).find_by("xpath", Elements(browser).page_link_on_navigation_menu(features)).click()
    time.sleep(2)
    return browser


@pytest.fixture(scope="function")
def video_feature_page(browser):
    Basemodel(browser).find_by("xpath", Elements(browser).page_link_on_navigation_menu(video)).click()
    time.sleep(2)
    Basemodel(browser).find_by("xpath", Elements(browser).page_link_on_navigation_menu(features)).click()
    time.sleep(2)
    return browser


