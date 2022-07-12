from ..JSONExtractor import JSONExtractor
import pathlib

def test_Extract_JSON_Value_Simple():
    currentDir = str(pathlib.Path(__file__).parent.absolute())
    jsonDoc = open(currentDir + '\\inputs\\updatePetResponse.json').read()
    jsonPath = '$.id'
    value = JSONExtractor().Extract_JSON_Value(jsonDoc, jsonPath)
    print(value)
    assert value == 1

def test_Extract_JSON_Value_Complex():
    currentDir = str(pathlib.Path(__file__).parent.absolute())
    jsonDoc = open(currentDir + '\\inputs\\updatePetResponse.json').read()
    jsonPath = '$.tags[0].name'
    value = JSONExtractor().Extract_JSON_Value(jsonDoc, jsonPath)
    print(value)
    assert value == 'german shepherd'

def test_Extract_JSON_Value_Array():
    currentDir = str(pathlib.Path(__file__).parent.absolute())
    jsonDoc = open(currentDir + '\\inputs\\updatePetResponse.json').read()
    jsonPath = '$.photoUrls[0]'
    value = JSONExtractor().Extract_JSON_Value(jsonDoc, jsonPath)
    print(value)
    assert value == 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg'


def test_Extract_JSON_Value_Object():
    currentDir = str(pathlib.Path(__file__).parent.absolute())
    jsonDoc = open(currentDir + '\\inputs\\updatePetResponse.json').read()
    jsonPath = '$.category.name'
    value = JSONExtractor().Extract_JSON_Value(jsonDoc, jsonPath)
    print(value)
    assert value == 'animal'

def test_Extract_JSON_Value_Filter():
    currentDir = str(pathlib.Path(__file__).parent.absolute())
    jsonDoc = open(currentDir + '\\inputs\\updatePetResponse.json').read()
    jsonPath = '$.tags[?(@.id == 1)].name'
    value = JSONExtractor().Extract_JSON_Value(jsonDoc, jsonPath)
    print(value)
    assert value == 'german shepherd'