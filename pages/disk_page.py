import time

from pages.base_page import BasePage
from pages.locators import DiskPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YadiskPage(BasePage):
    def __create_folder_window(self, folder_name):
        try:
            selector, locator = DiskPageLocators.INPUT_FOLDER_NAME_LINK
            el = WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((selector, locator)))
            el.send_keys(Keys.CONTROL + "a")
            el.send_keys(folder_name)
        except TimeoutException:
            raise AssertionError("Error while creating folder!")
        self.browser.find_element(*DiskPageLocators.SAVE_FOLDER_NAME_BUTTON).click()

    def create_folder(self, folder_name):
        self.create_resource()
        self.browser.find_element(*DiskPageLocators.CREATE_FOLDER_LINK).click()
        self.__create_folder_window(folder_name)

    def create_resource(self):
        try:
            selector, locator = DiskPageLocators.CREATE_LINK
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((selector, locator))).click()
        except TimeoutException:
            raise AssertionError("Create resource button is missing!")

    def find_file(self, file_name):
        try:
            selector, locator = DiskPageLocators.FIND_FILE_LINK
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((selector, locator.format(file_name))))
        except TimeoutException:
            raise AssertionError("Rename file error!")

    def get_context_file_menu(self, file_name):
        selector, locator = DiskPageLocators.FIND_FILE_LINK
        try:
            self.action.context_click(WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((selector, locator.format(file_name))))).perform()
        except TimeoutException:
            raise AssertionError("Error while opening file context menu!")

    def open_folder(self, folder_name):
        selector, locator = DiskPageLocators.OPEN_FOLDER_LINK
        try:
            self.action.double_click(WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((selector, locator.format(folder_name))))).perform()
        except TimeoutException:
            raise AssertionError("Created folder is missing!")

    def rename_file(self, file_name, new_file_name):
        self.get_context_file_menu(file_name)
        self.browser.find_element(*DiskPageLocators.CONTEXT_RENAME_LINK).click()

        selector, locator = DiskPageLocators.INPUT_FILE_NAME
        try:
            el = WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((selector, locator)))
        except TimeoutException:
            raise AssertionError("Error while renaming file!")
        time.sleep(1)  # TODO найти решение: ожидание для замены текста в поле, в Chrome не работает метод clear()
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(new_file_name)

        self.browser.find_element(*DiskPageLocators.SAVE_FILE_NAME_BUTTON).click()

    def status_upload(self):
        try:
            selector, locator = DiskPageLocators.UPLOAD_STATUS
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((selector, locator)))
        except TimeoutException:
            raise AssertionError("Error while uploading file!")
        self.browser.find_element(*DiskPageLocators.CLOSE_UPLOAD_TABLE).click()

    def upload_resource(self, resource_path):
        try:
            selector, locator = DiskPageLocators.UPLOAD_LINK
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((selector, locator))).send_keys(resource_path)
        except TimeoutException:
            raise AssertionError("Upload file error!")
