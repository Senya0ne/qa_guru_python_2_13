import requests
import pytest_voluptuous
from faker import Faker
import schemas.schemas as schema

URL = 'https://reqres.in'


def test_get_single_user():
    result: requests.Response = requests.get(url=f'{URL}/api/users/2')
    assert result.status_code == 200
    assert pytest_voluptuous.S(schema.get_single_user)


def test_post_user_create():
    fake = Faker()

    result: requests.Response = requests.post(url=f'{URL}/api/users/2',
                                              json={'name': fake.name(),
                                                    'job': fake.job()})

    assert result.status_code == 201
    assert pytest_voluptuous.S(schema.post_create_user)


def test_put_user_update():
    fake = Faker()
    name = fake.name()
    job = fake.job()

    result: requests.Response = requests.put(url=f'{URL}/api/users/2',
                                             json={'name': name,
                                                   'job': job})
    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert pytest_voluptuous.S(schema.update_user)


def test_patch_user_update():
    fake = Faker()
    name = fake.name()
    job = fake.job()

    result: requests.Response = requests.put(url=f'{URL}/api/users/2',
                                             json={'name': name,
                                                   'job': job})
    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert pytest_voluptuous.S(schema.update_user)


def test_delete_user():
    delete_result: requests.Response = requests.delete(url=f'{URL}/api/users/2')
    assert delete_result.status_code == 204
