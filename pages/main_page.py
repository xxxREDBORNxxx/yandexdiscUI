from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    URL = "https://ya.ru"

    def get_user_menu(self):
        try:
            selector, locator = MainPageLocators.USER_MENU
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((selector, locator))).click()
        except TimeoutException:
            raise AssertionError("User menu button is missing!")

    def go_to_disk_page(self, win_number):
        self.browser.find_element(*MainPageLocators.DISK_LINK).click()
        self.switch_browser_table(win_number)

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
