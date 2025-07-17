import os
from pytest_bdd import scenario
from steps.golf_steps import *
import allure

FEATURE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../features/golf.feature"))
print(f"Using feature file: {FEATURE_PATH}")



@allure.title("Search for Golf by name")
@allure.description("Verifies that the golf course 'Tiger Golf' appears in search results.")
@allure.severity(allure.severity_level.CRITICAL)
@scenario(FEATURE_PATH, "Search for Golf by name")
def test_search_name():
    pass


@allure.title("Search for Golf country in country")
@allure.description("Verifies that 'Canada' appears in search results.")
@allure.severity(allure.severity_level.CRITICAL)
@scenario(FEATURE_PATH, "Search for Golf country in country")
def test_search_country():
    pass
