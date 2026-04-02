import json
from pathlib import Path

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from ..pageObject.login_object import loginPage


scenarios(str(Path(__file__).resolve().parent.parent / "features" / "login.feature"))


@pytest.fixture(scope="session")
def global_config():
    file_path = Path(__file__).parent.parent / "data" / "global_config.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def base_url(global_config):
    return global_config["apps"]["sauce_demo_login"]


@given("the user opens the login page")
def user_opens_login_page(browser_instance):
    return browser_instance


@when(parsers.parse('the user attempts login for "{scenario}"'))
def attempt_login(browser_instance, configdata, test_context, scenario):
    scenario_data = configdata["login_scenarios"][scenario]
    test_context["scenario_data"] = scenario_data

    login_obj = loginPage(browser_instance)
    login_obj.login(scenario_data["username"], scenario_data["password"])


@then(parsers.parse('the login result for "{scenario}" should be correct'))
def verify_login_result(browser_instance, configdata, test_context, scenario):
    scenario_data = test_context.get("scenario_data")
    if scenario_data is None:
        scenario_data = configdata["login_scenarios"][scenario]

    login_obj = loginPage(browser_instance)
    login_obj.verify_login_result(scenario_data["expected"])
