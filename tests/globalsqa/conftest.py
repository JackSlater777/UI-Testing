import pytest
from selenium import webdriver
from config import selenium_grid_url


@pytest.fixture(params=["chrome", "edge"], scope="class")
def driver_init(request):

    if request.param == "chrome":
        driver = webdriver.Remote(
            command_executor=selenium_grid_url,
            options=webdriver.ChromeOptions()
        )
    if request.param == "edge":
        driver = webdriver.Remote(
            command_executor=selenium_grid_url,
            options=webdriver.EdgeOptions()
        )
    yield driver
    driver.quit()
