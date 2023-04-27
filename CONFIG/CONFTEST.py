import pytest

from selenium import webdriver

from CONFIG.CONFIG import TestData


@pytest.fixture(params=["chrome"])
def __init__driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()