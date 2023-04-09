from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def __input_login(self, login):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(login)

    def __input_password(self, password):
        try:
            selector, locator = LoginPageLocators.PASSWORD
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((selector, locator))).send_keys(password)
        except TimeoutException:
            raise AssertionError("Password input field is missing!")

    def __select_login_type(self):
        try:
            selector, locator = LoginPageLocators.MAIL_LINK
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((selector, locator))).click()
        except TimeoutException:
            raise AssertionError("Select login type button is missing!")

    def login(self, login, password):
        self.__select_login_type()
        self.browser.find_element(*LoginPageLocators.MAIL_LINK).click()
        self.__input_login(login)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        self.__input_password(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def select_mail_form(self):
        self.browser.find_element(*LoginPageLocators.MAIL_LINK).click()
