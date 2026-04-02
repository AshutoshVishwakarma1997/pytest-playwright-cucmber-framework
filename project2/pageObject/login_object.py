from playwright.sync_api import expect


class loginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.title = page.locator('[data-test="title"]')
        self.error_message = page.locator('[data-test="error"]')

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_result(self, expected):
        if expected["result"] == "success":
            expect(self.title).to_have_text(expected["title"])
            return

        expect(self.error_message).to_contain_text(expected["message"])
