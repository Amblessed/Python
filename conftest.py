import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")           # Run in headless mode
    options.add_argument("--start-maximized")    # Maximize the window
    web_driver = webdriver.Chrome(options=options)
    yield web_driver
    web_driver.quit()