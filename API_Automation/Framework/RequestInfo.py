
class RequestInfo:
    def __init__(self, requestId, url, method, requestHeaders, requestBody, expectedResponseBody, expectedStatusCode):
        self.requestId = requestId
        self.url = url
        self.method = method
        self.requestHeaders = requestHeaders
        self.requestBody = requestBody
        self.expectedResponseBody = expectedResponseBody
        self.expectedStatusCode = expectedStatusCode



