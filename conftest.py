import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('--language')
    options = Options()
    options.add_argument(f'--lang={language}')
    print(f'\nStart Chrome browser with language: {language}..')
    driver = webdriver.Chrome(options=options)
    yield driver
    print('\nQuit browser..')
    driver.quit()
