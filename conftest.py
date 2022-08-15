from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Choose the env: 'dev' or 'qa'"
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption('--env')


@fixture(scope='function')
def chrome_browser():
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)
    yield browser
    browser.quit()


@fixture(scope='function')
def firefox_browser():
    s = Service(GeckoDriverManager().install())
    browser = webdriver.Firefox(service=s)
    yield browser
    browser.quit()


@fixture(params=[webdriver.Chrome(service=Service(ChromeDriverManager().install())),
                 webdriver.Firefox(service=Service(GeckoDriverManager().install()))])
def cross_browser(request):
    driver = request.param
    yield driver
    driver.quit()


@fixture(scope='session')
def app_config(env):
    return Config(env)
