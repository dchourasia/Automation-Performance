from Framework.RequestInfo import RequestInfo
from Framework.libcommons import libcommons
import requests, json, traceback

class RequestProcessor:
    def Process_REST_Request(self, requestInfo:RequestInfo):
        try:
            if requestInfo.method == "GET":
                requestInfo.response = requests.get(requestInfo.url, headers=requestInfo.requestHeaders)
            elif requestInfo.method == "HEAD":
                requestInfo.response = requests.head(requestInfo.url, headers=requestInfo.requestHeaders)
            elif requestInfo.method == "POST":
                requestInfo.response = requests.post(requestInfo.url, headers=requestInfo.requestHeaders, data=requestInfo.requestBody)
            elif requestInfo.method == "PUT":
                requestInfo.response = requests.put(requestInfo.url, headers=requestInfo.requestHeaders, data=requestInfo.requestBody)
            elif requestInfo.method == "PATCH":
                requestInfo.response = requests.patch(requestInfo.url, headers=requestInfo.requestHeaders, data=requestInfo.requestBody)
            elif requestInfo.method == "DELETE":
                requestInfo.response = requests.delete(requestInfo.url, headers=requestInfo.requestHeaders, data=requestInfo.requestBody)

            try:
                if requestInfo.response.json():
                    requestInfo.responseBody = json.dumps(requestInfo.response.json(), indent=4)
                    if libcommons.mode != 'dev':
                        libcommons.run_keyword("log", "${requestInfo.responseBody}")
            except:
                if requestInfo.response.text:
                    requestInfo.responseBody = requestInfo.response.text
                    if libcommons.mode != 'dev':
                        libcommons.run_keyword("log", "${requestInfo.responseBody}")


            requestInfo.responseHeaders = json.dumps(dict(requestInfo.response.headers), indent=4)
            if libcommons.mode != 'dev':
                libcommons.run_keyword("log", "${requestInfo.responseHeaders}")

            requestInfo.responseStatusCode = requestInfo.response.status_code
            if libcommons.mode != 'dev':
                libcommons.run_keyword("log", "${requestInfo.responseStatusCode}")

        except Exception as e:
            print(traceback.format_exc())
            raise e
        return requestInfo
