import json
from pathlib import Path

import pytest

from ..pageObject.login_object import loginPage


@pytest.fixture(scope="session")
def global_config():
    file_path = Path(__file__).parent.parent / "data" / "global_config.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def base_url(global_config):
    return global_config["apps"]["sauce_demo_login"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "scenario_name",
    ["happy_flow", "invalid_credentials", "empty_username", "empty_password"],
)
def test_login_page(browser_instance, configdata, scenario_name):
    scenario = configdata["login_scenarios"][scenario_name]
    login_obj = loginPage(browser_instance)

    login_obj.login(scenario["username"], scenario["password"])
    login_obj.verify_login_result(scenario["expected"])
