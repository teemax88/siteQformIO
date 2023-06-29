import pytest
from selenium import webdriver


@pytest.fixture(params=["Chrome"], scope="module")
def driver(request):
    if request.param == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()


@pytest.fixture(scope="class")
def check(request, driver):
    request.cls.driver = driver
    yield


@pytest.mark.usefixtures("check")
class TestRequestObject:
    def test_of_check_request(self):
        print(f'Вызываем драйвер -- {self.driver}')
