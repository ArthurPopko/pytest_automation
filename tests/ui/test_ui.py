from pytest import mark


@mark.dev
def test_env_is_dev(cross_browser, app_config, env):
    base_url = app_config.base_url
    port = app_config.app_port
    cross_browser.get(base_url)
    assert env == 'dev'
    assert base_url == 'http://google.com'
    assert port == 8080


@mark.qa
def test_env_is_qa(cross_browser, app_config, env):
    base_url = app_config.base_url
    port = app_config.app_port
    cross_browser.get(base_url)
    assert env == 'qa'
    assert base_url == 'http://mail.ru'
    assert port == 80
