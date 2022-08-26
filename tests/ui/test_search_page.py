import allure
from pytest import mark

from tests.page_object.google_search_page import GoogleSearchPage
from tests.page_object.mail_search_page import MailSearchPage


@mark.ui
@mark.dev
def test_google_search_env_dev(chrome_browser, app_config, load_test_data, env):
    base_url = app_config.base_url
    port = app_config.app_port
    input_text = load_test_data.get('input1')
    expected_text = 'data1'
    google_search_page = GoogleSearchPage(driver=chrome_browser)
    with allure.step(f'Open browser'):
        chrome_browser.get(base_url)
    with allure.step(f'Input: "{input_text}"'):
        google_search_page.search_input.input_text(input_text)
    with allure.step(f'Search for: "{input_text}"'):
        google_search_page.search_button.click()

    assert env == 'dev'
    assert base_url == 'http://google.com'
    assert port == 8080
    assert google_search_page.search_input.attribute('value') == expected_text


@mark.xfail(reason='not qa env')
@mark.ui
@mark.qa
def test_mail_search_env_qa(chrome_browser, load_test_data, app_config, env):
    base_url = app_config.base_url
    port = app_config.app_port
    input_text = load_test_data.get('input1')
    expected_text = 'data11'
    with allure.step(f'Open browser'):
        mail_search_page = MailSearchPage(driver=chrome_browser)
        chrome_browser.get(base_url)
    with allure.step(f'Input: "{input_text}"'):
        mail_search_page.search_input.input_text(input_text)
    with allure.step(f'Search for: "{input_text}"'):
        mail_search_page.search_button.click()

    assert env == 'qa'
    assert base_url == 'http://mail.ru'
    assert port == 80
    assert mail_search_page.search_input_result.attribute('value') == expected_text
