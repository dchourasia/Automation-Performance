import json

from ..RequestProcessor import RequestProcessor
from ..BaselineValidator import BaselineValidator
from ..RequestInfo import RequestInfo
import pathlib


def test_Process_REST_Request_GET():
    _requestInfo = RequestInfo('Get All Users', 'https://reqres.in/api/users', method='GET', requestHeaders={'Accept': 'application/json'}, requestBody={},
                               expectedResponseBody={}, expectedStatusCode=200)

    RequestProcessor().Process_REST_Request(_requestInfo)
    assert _requestInfo.expectedStatusCode == _requestInfo.responseStatusCode

def test_Process_REST_Request_HEAD():
    _requestInfo = RequestInfo('Get All Users', 'https://reqres.in/api/users', method='HEAD',
                               requestHeaders={'Accept': 'application/json'}, requestBody={}, expectedResponseBody={}, expectedStatusCode=200)

    RequestProcessor().Process_REST_Request(_requestInfo)
    assert _requestInfo.expectedStatusCode == _requestInfo.responseStatusCode


def test_Process_REST_Request_POST():
    _requestInfo = RequestInfo('Create User', 'https://reqres.in/api/users', method='POST',
                               requestHeaders={'Content-Type': 'application/json', 'Accept': 'application/json'},
                               requestBody=json.dumps({"name": "deepak", "job": "automation"}), expectedResponseBody={}, expectedStatusCode=201)

    RequestProcessor().Process_REST_Request(_requestInfo)
    assert _requestInfo.expectedStatusCode == _requestInfo.responseStatusCode


def test_Process_REST_Request_PUT():
    _requestInfo = RequestInfo('Update User', 'https://reqres.in/api/users/2', method='PUT',
                               requestHeaders={'Content-Type': 'application/json', 'Accept': 'application/json'},
                               requestBody=json.dumps({"name": "deepak", "job": "automation"}), expectedResponseBody={}, expectedStatusCode=200)

    RequestProcessor().Process_REST_Request(_requestInfo)
    assert _requestInfo.expectedStatusCode == _requestInfo.responseStatusCode


def test_Process_REST_Request_DELETE():
    _requestInfo = RequestInfo('Delete User', 'https://reqres.in/api/users/2', method='DELETE',
                               requestHeaders={}, requestBody={},
                               expectedResponseBody={}, expectedStatusCode=204)

    RequestProcessor().Process_REST_Request(_requestInfo)
    assert _requestInfo.expectedStatusCode == _requestInfo.responseStatusCode