import json
from pathlib import Path

import pytest
from playwright.sync_api import Playwright


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="browser name",
    )

@pytest.fixture(scope="session")
def configdata():
    file_path = Path(__file__).parent.parent / "data" / "login_config.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def browser_instance(playwright: Playwright, base_url, request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()
    page.goto(base_url)
    yield page
    context.close()
    browser.close()


@pytest.fixture
def test_context():
    return {}
