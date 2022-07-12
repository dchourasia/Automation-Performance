from ..BaselineValidator import BaselineValidator
from ..RequestInfo import RequestInfo
import pathlib, json

def test_Validate_Response_Body():
    _requestInfo = RequestInfo('Unit Test', 'http://www.google.com', method='GET', requestHeaders={'Accept': 'application/json'}, requestBody={},
                               expectedResponseBody={}, expectedStatusCode=200)
    currentDir = str(pathlib.Path(__file__).parent.absolute())
    _requestInfo.responseBody = open(currentDir + '\\inputs\\updatePetResponse.json').read()
    _requestInfo.expectedResponseBody = open(currentDir + '\\baselines\\updatePetBaseline.json').read()

    diff = BaselineValidator().Validate_Response_Body(_requestInfo)
    print(diff)
    assert len(diff) == 1 and 'Value does not match for item at .category.name , expected is bird, but actual is animal' in diff

def test_Compare_JSON():
    currentDir = str(pathlib.Path(__file__).parent.absolute())
    response = json.load(open(currentDir + '\\inputs\\updatePetResponse.json'))
    baseline = json.load(open(currentDir + '\\baselines\\updatePetBaseline.json'))
    diff = []
    BaselineValidator().Compare_JSON(response, baseline, diff)
    print(diff)
    assert len(diff) == 1 and 'Value does not match for item at .category.name , expected is bird, but actual is animal' in diff





