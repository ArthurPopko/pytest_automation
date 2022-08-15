from pytest import mark


from tests.page_object.google_search_page import GoogleSearchPage


@mark.dev
def test_env_is_dev(cross_browser, app_config, env):
    base_url = app_config.base_url
    port = app_config.app_port
    # open google search page:
    google_search_page = GoogleSearchPage(driver=cross_browser)
    cross_browser.get(base_url)
    # input search request
    google_search_page.search_input.input_text('123')
    # click search
    google_search_page.search_button.click()

    assert env == 'dev'
    assert base_url == 'http://google.com'
    assert port == 8080
    assert google_search_page.search_input.attribute('value') == '123'
