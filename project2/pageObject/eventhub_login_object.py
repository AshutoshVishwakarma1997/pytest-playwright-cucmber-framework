from playwright.sync_api import Page, expect


class EventHubLoginPage:
    def __init__(self, page:Page):
        self.page = page

    def login(self, username, password):
        self.page.get_by_placeholder("you@email.com").fill(username)
        self.page.get_by_placeholder("••••••").fill(password)
        self.page.locator("#login-btn").click()
        expect(
            self.page.get_by_role("heading", name="Discover & Book Amazing Events")
        ).to_be_visible()
        print("EventHub home heading is visible")