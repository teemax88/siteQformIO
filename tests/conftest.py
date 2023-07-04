import pytest
import time

from src.utils.methods import BaseMethods
from variables import *
from pom.BasePage.basemodel import Basemodel
from src.locators.builder import Elements

# """Переход на страницу Формы из меню навигации"""


@pytest.fixture(scope="class")
def forms_page(request, browser):
    BaseMethods(browser).find_by("xpath", Elements().page_link_on_navigation_menu(forms)).click()
    time.sleep(2)
    request.cls.driver = browser
    yield


@pytest.fixture(scope="class")
def quiz_page(request, browser):
    Basemodel(browser).find_by("xpath", Elements().page_link_on_navigation_menu(quiz)).click()
    time.sleep(2)
    request.cls.driver = browser
    yield


@pytest.fixture(scope="class")
def video_page(request, browser):
    Basemodel(browser).find_by("xpath", Elements().page_link_on_navigation_menu(video)).click()
    time.sleep(2)
    request.cls.driver = browser
    yield


"""Переход на страницу Возможности"""


@pytest.fixture(scope="class")
def forms_feature_page(request, browser):
    Basemodel(browser).find_by("xpath", Elements().page_link_on_navigation_menu(forms)).click()
    time.sleep(2)
    Basemodel(browser).find_by("xpath", Elements().page_link_on_navigation_menu(features)).click()
    time.sleep(2)
    request.cls.driver = browser
    yield


@pytest.fixture(scope="class")
def quiz_feature_page(request, browser):
    Basemodel(browser).find_by("xpath", Elements().page_link_on_navigation_menu(quiz)).click()
    time.sleep(2)
    Basemodel(browser).find_by("xpath", Elements().page_link_on_navigation_menu(features)).click()
    time.sleep(2)
    request.cls.driver = browser
    yield


@pytest.fixture(scope="class")
def video_feature_page(request, browser):
    Basemodel(browser).find_by("xpath", Elements().page_link_on_navigation_menu(video)).click()
    time.sleep(2)
    Basemodel(browser).find_by("xpath", Elements().page_link_on_navigation_menu(features)).click()
    time.sleep(2)
    request.cls.driver = browser
    yield
