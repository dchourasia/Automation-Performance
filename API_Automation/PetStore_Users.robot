*** Settings ***
Library     Collections
Library     Framework/RESTLibrary.py          WITH NAME   RESTLibrary
Library     Framework/JSONExtractor.py        WITH NAME   JSONExtractor
Library     Process
Library     Collections
Library     OperatingSystem
Library     DateTime


*** Test Cases ***
Create multiple users with array
    [Tags]  dev     poc     demo
    Make REST Request  Create Multiple Users    https://petstore.swagger.io/v2/user/createWithArray   method=POST
    ...     requestHeaders={'Content-Type': 'application/json', 'Accept' : 'application/json'}
    ...     requestBody=${EXECDIR}/Inputs/createUsers.json      expectedStatusCode=200
    ...     expectedResponseBody=${EXECDIR}/Baselines/createUsersBaseline.json

Update a user's username and other details
    [Tags]  dev     poc     demo
    Make REST Request  Update User    https://petstore.swagger.io/v2/user/deepak.chourasia   method=PUT
    ...     requestHeaders={'Content-Type': 'application/json', 'Accept' : 'application/json'}
    ...     requestBody=${EXECDIR}/Inputs/updateUser.json      expectedStatusCode=200
    ...     expectedResponseBody=${EXECDIR}/Baselines/updateUserBaseline.json

Get user by the updated username
    [Tags]  dev     poc     demo
    Make REST Request  Get User    https://petstore.swagger.io/v2/user/deepak.chourasia.modified   method=GET
    ...     requestHeaders={'Accept' : 'application/json'}      expectedStatusCode=200
    ...     expectedResponseBody=${EXECDIR}/Baselines/getUserBaseline.json