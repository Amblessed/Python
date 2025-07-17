import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    web_driver = webdriver.Chrome(options=options)
    yield web_driver
    web_driver.quit()