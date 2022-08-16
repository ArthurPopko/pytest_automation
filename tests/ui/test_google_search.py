from pytest import mark


from tests.page_object.google_search_page import GoogleSearchPage


@mark.ui
def test_env_is_dev(chrome_browser, app_config, env, load_test_data):
    # open google search page:
    base_url = app_config.base_url
    port = app_config.app_port
    input_text = load_test_data.get('input1')
    expected_text = 'data1'
    google_search_page = GoogleSearchPage(driver=chrome_browser)
    chrome_browser.get(base_url)
    # input search request
    google_search_page.search_input.input_text(input_text)
    # click search
    google_search_page.search_button.click()

    assert env == 'dev'
    assert base_url == 'http://google.com'
    assert port == 8080
    assert google_search_page.search_input.attribute('value') == expected_text

