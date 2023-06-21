import pytest
from selenium import webdriver
from variables import URL


# "Chrome", "Firefox", "Opera", "Edge", "internet explorer", "Safari"
@pytest.fixture(params=["Chrome"], scope="function")
def browser(request):
    if request.param == "Chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Chrome(options=options)

        driver.maximize_window()
        driver.get(URL)
        driver.delete_all_cookies()
        driver.set_page_load_timeout(10)
        yield driver

        driver.quit()
