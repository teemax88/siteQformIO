from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


class Utils:
    @staticmethod
    def join_strings(str_list: List[str]) -> str:
        return ",".join(str_list)


class BaseMethods(Utils):
    def __init__(self, driver):
        self.driver = driver
        self.ignored_exceptions = (StaleElementReferenceException, TimeoutException)
        self.__wait = WebDriverWait(driver, 10, 0.3, ignored_exceptions=self.ignored_exceptions)

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME
        }
        return locating[find_by]

    """Операции с одиночными элементами"""

    def is_visible(self, find_by: str, locator: str) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)))

    def is_clickable(self, find_by: str, locator: str) -> WebElement:
        return self.__wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)))

    def is_present(self, find_by: str, locator: str) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)))

    def get_text_from_one_element(self, element: WebElement) -> str:
        return element.text.strip()

    def find_by(self, find_by: str, locator: str) -> WebElement:
        return self.driver.find_element(self.__get_selenium_by(find_by), locator)

    def find_and_get_text(self, find_by: str, locator: str) -> str:
        return self.driver.find_element(self.__get_selenium_by(find_by), locator).text.strip()

    def find_and_get_attribute(self, find_by: str, locator: str, attribute: str) -> str:
        return self.driver.find_element(self.__get_selenium_by(find_by), locator).get_attribute(attribute)

    def is_not_present(self, find_by: str, locator: str) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)))

    def get_attribute_from_one_element(self, attribute: str, element: WebElement) -> str:
        return element.get_attribute(attribute)

    """Операции с несколькими элементами"""

    def are_visible(self, find_by: str, locator: str) -> List[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)))

    def are_present(self, find_by: str, locator: str) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)))

    def get_text_all_webelements(self, elements: List[WebElement]) -> List[str]:
        return [element.text.strip() for element in elements]

    def finds_by(self, find_by: str, locator: str) -> List[WebElement]:
        return self.driver.find_elements(self.__get_selenium_by(find_by), locator)
