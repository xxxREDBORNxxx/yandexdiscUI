from pages.locators import BasePageLocators


class BasePage:
    URL = None

    def __init__(self, browser, action, timeout=60):
        self.browser = browser
        self.timeout = timeout
        self.action = action

    def logout_user(self):
        self.user_account()
        self.browser.find_element(*BasePageLocators.LOGOUT_LINK).click()

    def open(self):
        self.browser.get(self.URL)

    def switch_browser_table(self, number):
        self.browser.switch_to.window(self.browser.window_handles[number])

    def user_account(self):
        self.browser.find_element(*BasePageLocators.USER_LINK).click()
