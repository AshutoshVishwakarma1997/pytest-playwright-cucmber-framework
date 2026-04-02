import json
from pathlib import Path

import pytest
from pytest_bdd import given, scenarios, then, when

from ..pageObject.eventhub_booking_object import EventHubBookingPage
from ..pageObject.eventhub_login_object import EventHubLoginPage


scenarios(str(Path(__file__).resolve().parent.parent / "features" / "eventhub.feature"))


@pytest.fixture(scope="session")
def global_config():
    file_path = Path(__file__).parent.parent / "data" / "global_config.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def event_booking_data():
    file_path = Path(__file__).parent.parent / "data" / "event_booking_config.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def base_url(global_config):
    return global_config["apps"]["event_booking_url"]


@pytest.fixture
def booking_scenario(event_booking_data):
    return event_booking_data["booking_scenarios"]["happy_path_booking"]


@given("the user opens the EventHub login page")
def open_eventhub_login_page(browser_instance):
    return browser_instance


@when("the user logs in with valid EventHub credentials")
def login_to_eventhub(browser_instance, booking_scenario, test_context):
    login_page = EventHubLoginPage(browser_instance)
    login_page.login(booking_scenario["username"], booking_scenario["password"])
    test_context["booking_scenario"] = booking_scenario


@when("the user selects the configured event")
def select_configured_event(browser_instance, booking_scenario):
    booking_page = EventHubBookingPage(browser_instance)
    booking_page.select_event(booking_scenario["event_name"])


@when("the user completes the booking")
def complete_booking(browser_instance, booking_scenario):
    booking_page = EventHubBookingPage(browser_instance)
    booking_page.complete_booking(
        customer_name=booking_scenario["customer_name"],
        email=booking_scenario["email"],
        phone=booking_scenario["phone"]
    )


@then("the booking should be confirmed")
def verify_booking(browser_instance, booking_scenario, test_context):
    scenario = test_context.get("booking_scenario", booking_scenario)
    booking_page = EventHubBookingPage(browser_instance)
    booking_page.verify_booking_result(scenario["expected"])
