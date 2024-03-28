import pytest
import unittest.mock as mock
import service

@mock.patch("requests.get")
def test_get_users_internal(mocked_requests_get):
    mocked_users = mock.Mock()
    mocked_users.status_code = 200
    mocked_users.json.return_value = {"id": 1,  "name": "Elvis"}
    mocked_requests_get.return_value = mocked_users
    real_service = service.Service()
    assert real_service.get_users().status_code == 200
