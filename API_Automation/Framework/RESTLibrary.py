from Framework.RequestInfo import RequestInfo
from Framework.libcommons import libcommons

class RESTLibrary:

    def Make_REST_Request(self, requestId, url, method='GET', requestHeaders={}, requestBody="", expectedResponseBody="", expectedStatusCode=200):
        requestInfo = RequestInfo(requestId, url, method, requestHeaders, requestBody, expectedResponseBody, expectedStatusCode)
        libcommons.robotBuiltIn.set_suite_variable("${requestInfo}", requestInfo)

        requestInfo = libcommons.run_keyword("Generate REST Request", "${requestInfo}", library='${EXECDIR}/Framework/InputGenerator.py')
        libcommons.robotBuiltIn.set_suite_variable("${requestInfo}", requestInfo)

        requestInfo = libcommons.run_keyword("Process REST Request", "${requestInfo}", library='${EXECDIR}/Framework/RequestProcessor.py')
        libcommons.robotBuiltIn.set_suite_variable("${requestInfo}", requestInfo)

        requestInfo = libcommons.run_keyword("Validate Response Against Baselines", "${requestInfo}", library='${EXECDIR}/Framework/BaselineValidator.py')
        libcommons.robotBuiltIn.set_suite_variable("${requestInfo}", requestInfo)

        return requestInfo



