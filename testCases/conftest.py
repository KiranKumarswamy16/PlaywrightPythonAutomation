import pytest
import time
from playwright.sync_api import sync_playwright

SITE_MAP = {
    "google": "https://www.google.com",
    "facebook": "https://www.facebook.com/login/",
    "github": "https://github.com/login",
    "amazon": "https://www.amazon.in/",
    "demoapp": "https://demo.automationtesting.in/Register.html",
    "internethero": "https://the-internet.herokuapp.com/javascript_alerts",
    "paytm": "https://paytm.com/"
    # Add more sites here
}

# 🛠 Add CLI option
def pytest_addoption(parser):
    parser.addoption(
        "--site", action="store", default="google", help="Site alias to test (e.g., google, facebook, github)"
    )

# 🌐 Return the full site URL based on the alias
@pytest.fixture(scope="function")
def site_url(request):
    site_alias = request.config.getoption("--site").lower()
    url = SITE_MAP.get(site_alias)
    if not url:
        raise ValueError(f"Invalid site alias '{site_alias}'. Valid options: {list(SITE_MAP.keys())}")
    return url

# 🚀 Launch browser
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, args=["--start-maximized"])  ## to maximize
        time.sleep(2)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser, site_url):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto(site_url)
    page.wait_for_timeout(1500)
    yield context, page
    page.close()



