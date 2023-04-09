import pytest
import configparser
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # выбора браузера при запуске из терминала "--browser_name=<браузер>"
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope='session')
def action(browser):
    return ActionChains(browser)


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


@pytest.fixture(scope='session')
def login(config):
    return config['User']['login']


@pytest.fixture(scope='session')
def password(config):
    return config['User']['password']