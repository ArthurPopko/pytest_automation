from pytest import mark


@mark.api
def test_api_dev(app_config, env):
    base_url = app_config.base_url
    port = app_config.app_port

    assert env == 'dev'
    assert base_url == 'http://google.com'
    assert port == 8080


# use "-rsx" flag to see skipped and failed reason
# @mark.skip(reason='qa env only')
@mark.xfail(reason='not qa env')
@mark.api
def test_api_qa(app_config, env):
    base_url = app_config.base_url
    port = app_config.app_port

    assert env == 'qa'
    assert base_url == 'http://mail.ru'
    assert port == 80
