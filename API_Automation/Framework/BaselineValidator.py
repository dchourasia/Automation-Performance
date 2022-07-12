import json
from Framework.RequestInfo import RequestInfo
from Framework.libcommons import libcommons

class BaselineValidator:
    def Validate_Response_Body(self, requestInfo:RequestInfo):
        requestInfo.diff = []
        if requestInfo.expectedResponseBody:
            requestInfo.expectedResponseBody = open(requestInfo.expectedResponseBody).read() if libcommons.path_exists(
                libcommons.sanitizeFilePath(requestInfo.expectedResponseBody)) else requestInfo.expectedResponseBody
            self.Compare_JSON(json.loads(requestInfo.responseBody), json.loads(requestInfo.expectedResponseBody), requestInfo.diff)

            if libcommons.mode != 'dev':
                libcommons.run_keyword("log", "${requestInfo.expectedResponseBody}")
                if requestInfo.diff:
                    libcommons.run_keyword("log list", "${requestInfo.diff}")
                    raise Exception("ResponseBodyVerificationFailureError")
        return requestInfo.diff


    def Compare_JSON(self, response, baseline, diff, parentPath=''):
        if type(baseline) == dict:
            for item in baseline:
                if item in response:
                    self.Compare_JSON(response[item], baseline[item], diff, parentPath + "." + item)
                else:
                    diff.append('item with key {item} is missing from response'.format(item=parentPath + "." + item))
        elif type(baseline) == list:
            for index, item in enumerate(baseline):
                if index < len(response):
                    self.Compare_JSON(response[index], baseline[index], diff, parentPath + ".[" + str(index) + "]")
                else:
                    diff.append('item with key {item} is missing from response'.format(item=parentPath + "." + item))
        else:
            if baseline != response:
                diff.append('Value does not match for item at {parentPath} , expected is {expected}, but actual is {actual}'.format(parentPath=parentPath, expected=baseline, actual=response))


    def Validate_Status_Code(self, requestInfo:RequestInfo):
        try:
            if libcommons.mode != 'dev':
                libcommons.run_keyword("should be equal as strings", requestInfo.response.status_code, requestInfo.expectedStatusCode)
        except Exception as e:
            raise Exception("StatusCodeVerificationFailureError")
        return requestInfo.response.status_code == requestInfo.expectedStatusCode

    def Validate_Response_Against_Baselines(self, requestInfo:RequestInfo):
        if requestInfo.expectedResponseBody and libcommons.mode != 'dev':
            libcommons.run_keyword("Validate Response Body", "${requestInfo}")
        if libcommons.mode != 'dev':
            libcommons.run_keyword("Validate Status Code", "${requestInfo}")
        return requestInfo
