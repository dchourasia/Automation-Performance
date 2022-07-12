
High Level Overview
---
Test Automation:

* Automation Tool Used : **Robot Framework**
* Programming Language : **Python**
* Custom Framework Developed : **RESTLibrary**
* TestSuites
  * PetStore_Pets.robot
  * PetStore_Users.robot
* Framework Code : inside **Framework** directory
* **runRobot.bat** : to execute automation tests
* [Automation Report](https://github.com/dchourasia/Automation-Performance/tree/main/API_Automation/robot_report): in **robot_report** folder

Unit Tests:
* Unit Testing Framework: **pytest**
* Location : inside **Framework/test** directory
* **runPyTest.bat** : to execute unit tests
* [Unit Test Report](https://github.com/dchourasia/Automation-Performance/tree/main/API_Automation/pytest_report): in **pytest_report** folder


Common:
* config.json
  * mode=prod - for executing robot tests
  * mode=dev - for executing unit tests
* the mode needs to be set because REST-Library accesses robot-runtime context which is only available when the library is used from robot-framework


RESTLibrary
---
RESTLibrary is designed and developed with a thought process to eliminate all the repetitive efforts while performing end-to-end REST API Automation using Robot Framework.
Though **current scope is small** only limited to achieving automation of current set of tests.
Below are the high level description about RESTLibrary:
* Developed using Object-Oriented architecture
* Developed in a scalable way with a separate components for each independent step
* High Level Features:
  * Support of making any REST call using **single keyword**
  * Support of **all the HTTP verbs** - GET, POST, HEAD, PUT, PATCH, DELETE
  * Support for **dynamic input generation**, we can provide file-path or request body
  * Support for **JSON Benchmarking/Baselining**, we can simply provide the baseline json and framework will ensure to compare it with response
  * Support of JSON **node extraction using JSON-Path**, which can be used for correlating data between various endpoints
* Current components:
  * Request-Info : this makes our entire framework Object-Oriented by building a cetral request-info object, which has all the details about the current request over its life-cycle 
  * Input-Generator : takes care of generating the request-body, endpoint URL and request headers, it can be extended to many more features where we can correlate the parameters and have dynamic variable references along with file upload etc
  * Request-Processor : this takes care of executing all the REST requests based on the details in the request-info object, it masks all the details of how requests are executed along with exception handling
  * Baseline-Validator : this has a generic JSON-comparison feature using which we compare the API response with expected baseline to ensure that our API is working fine
  * JSON-Extractor : this exposes a generic feature to extract value at given jsonPath in given json
  