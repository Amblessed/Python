import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pytest_bdd import given, when, then, parsers


@given("I start the browser")
def start_browser():
    print("Browser started")

@when(parsers.parse('I go to "{url}"'))
def go_to_url(driver, url):
    print(f"Opening URL: {url}")
    driver.get(url)
    time.sleep(2)

@when(parsers.parse('I type "{text}" in the search box'))
def type_in_search_box(driver, text):
    print(f"Typing '{text}' in the search box")
    search_box = driver.find_element(By.NAME, "SearchString")
    search_box.send_keys(text)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

@then(parsers.parse('I should see golf course "{course_name}"'))
def should_see_course(driver, course_name):
    print(f"Verifying that the golf course '{course_name}' appears in search results")
    result = driver.find_element(By.XPATH, "/html/body/div[1]/main/table[2]/tbody/tr/td[1]")
    assert course_name == result.text

@when(parsers.parse('I select "{country}" in the dropdown list'))
def select_country(driver, country):
    print(f"Selecting country '{country}' from the dropdown")
    country_dropdown = driver.find_element(By.NAME, "CurrentFilter")
    country_dropdown.send_keys(country)
    search_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/table[1]/tbody/tr/td[2]/form/fieldset/button")
    search_button.click()
    time.sleep(2)

@then(parsers.parse('I should see golf course in the country "{nation}"'))
def should_see_country_course(driver, nation):
    print(f"Verifying that the golf course appears in the country '{nation}'")
    country_result = driver.find_element(By.XPATH, "/html/body/div[1]/main/table[2]/tbody/tr[1]/td[2]")
    assert nation in country_result.text
