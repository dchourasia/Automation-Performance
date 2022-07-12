*** Settings ***
Library     Collections
Library     Framework/RESTLibrary.py          WITH NAME   RESTLibrary
Library     Framework/JSONExtractor.py        WITH NAME   JSONExtractor
Library     Process
Library     Collections
Library     OperatingSystem
Library     DateTime


*** Test Cases ***
Create multiple pets
    [Tags]  dev     poc     demo
    Make REST Request  Create Pet - Dog    https://petstore.swagger.io/v2/pet   method=POST
    ...     requestHeaders={'Content-Type': 'application/json', 'Accept' : 'application/json'}
    ...     requestBody=${EXECDIR}/Inputs/createPet_dog.json      expectedStatusCode=200
    ...     expectedResponseBody=${EXECDIR}/Baselines/createPetDogBaseline.json

    Make REST Request  Create Pet - Parrot    https://petstore.swagger.io/v2/pet   method=POST
    ...     requestHeaders={'Content-Type': 'application/json', 'Accept' : 'application/json'}
    ...     requestBody=${EXECDIR}/Inputs/createPet_parrot.json      expectedStatusCode=200
    ...     expectedResponseBody=${EXECDIR}/Baselines/createPetParrotBaseline.json


Update pet's status and other details
    [Tags]  dev     poc     demo
    Make REST Request  Update Pet - Dog    https://petstore.swagger.io/v2/pet   method=PUT
    ...     requestHeaders={'Content-Type': 'application/json', 'Accept' : 'application/json'}
    ...     requestBody=${EXECDIR}/Inputs/updatePet_dog.json      expectedStatusCode=200
    ...     expectedResponseBody=${EXECDIR}/Baselines/updatePetDogBaseline.json

Get pet by status and verify updated status of pet
    [Tags]  dev     poc     demo
    ${requestInfo}=     Make REST Request  Get pets by status    https://petstore.swagger.io/v2/pet/findByStatus?status=sold   method=GET
    ...     requestHeaders={'Accept' : 'application/json'}      expectedStatusCode=200
    Log  ${requestInfo.responseBody}

    ${pet status}=      Extract JSON Value      ${requestInfo.responseBody}         $[?(@.id == 1)].status

    Should Be Equal As Strings      ${pet status}       sold