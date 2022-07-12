from jsonpath_ng.ext import parser
import json

class JSONExtractor:

    def Extract_JSON_Value(self, jsonDoc, jsonPath):
        print('jsonPath', jsonPath)
        if type(jsonDoc) == str:
            jsonDoc = json.loads(jsonDoc)
        matches = parser.ExtentedJsonPathParser().parse(jsonPath.replace(' && ', ' & ')).find(jsonDoc)
        # matches = jsonpath(jsonDoc, jsonPath)
        return matches[0].value if matches else None




