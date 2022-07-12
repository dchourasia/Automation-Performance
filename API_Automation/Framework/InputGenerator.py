from Framework.RequestInfo import RequestInfo
from Framework.libcommons import libcommons

class InputGenerator:
    def Generate_URL(self, requestInfo:RequestInfo):
        if requestInfo.url and libcommons.mode != 'dev':
            libcommons.run_keyword('log', "${requestInfo.url}")

    def Generate_Request_Body(self, requestInfo:RequestInfo):
        requestInfo.requestBody = open(requestInfo.requestBody).read() if libcommons.path_exists(libcommons.sanitizeFilePath(requestInfo.requestBody)) else requestInfo.requestBody

        if libcommons.mode != 'dev':
            libcommons.run_keyword('log', "${requestInfo.requestBody}")

    def Generate_Request_Headers(self, requestInfo:RequestInfo):
        if requestInfo.requestHeaders and libcommons.mode != 'dev':
            libcommons.run_keyword('log', "${requestInfo.requestHeaders}")

    def Generate_REST_Request(self, requestInfo:RequestInfo):
        if libcommons.mode != 'dev':
            libcommons.run_keyword('Generate URL', "${requestInfo}")
            if requestInfo.requestHeaders:
                libcommons.run_keyword('Generate Request Headers', "${requestInfo}")
            if requestInfo.requestBody:
                libcommons.run_keyword('Generate Request Body', "${requestInfo}")
        return requestInfo




