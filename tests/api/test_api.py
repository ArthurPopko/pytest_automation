import requests
from pytest import mark
from pytest_testrail.plugin import pytestrail


@mark.api
@pytestrail.case('C5')
def test_get_user_dev(app_config, env):
    url = f'{app_config.api_url}/api/users/2'
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    result = response.json()
    user_id = result['data']['id']
    first_name = result['data']['first_name']
    last_name = result['data']['last_name']
    email = result['data']['email']

    assert env == 'dev'
    assert user_id == 2
    assert first_name == 'Janet'
    assert last_name == 'Weaver'
    assert email == 'janet.weaver@reqres.in'


@mark.api
@pytestrail.case('C2')
def test_post_user_dev(app_config, env):
    url = f'{app_config.api_url}/api/users'
    headers = {
        'Content-Type': 'application/json'
    }

    body = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(url, headers=headers, json=body)

    result = response.json()
    first_name = result['name']
    job = result['job']

    assert env == 'dev'
    assert response.status_code == 201
    assert first_name == 'morpheus'
    assert job == 'leader'


@mark.api
@pytestrail.case('C3')
def test_login_dev(app_config, env):
    url = f'{app_config.api_url}/api/login'

    headers = {
        'Content-Type': 'application/json'
    }

    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(url, headers=headers, json=body)
    user_token = response.json()['token']

    assert env == 'dev'
    assert response.status_code == 200
    assert user_token == 'QpwL5tke4Pnpja7X4'


@mark.api
@pytestrail.case('C4')
def test_login_sad_path(app_config, env):
    url = f'{app_config.api_url}/api/login'

    headers = {
        'Content-Type': 'application/json'
    }

    body = {
        "email": "peter@klaven",
    }

    response = requests.post(url, headers=headers, json=body)
    login_error = response.json()['error']

    assert env == 'dev'
    assert response.status_code == 400
    assert login_error == 'Missing password'
