import json
import jsonschema
from jsonschema import validate, Draft6Validator, Draft7Validator
import glob


def validate_cmarker_created(jsonData):
    try:
        with open('schema/cmarker_created.schema') as schema: 
            jsonSchema = json.load(schema)
            validate(instance=jsonData, schema=jsonSchema)
            #Draft6Validator(jsonSchema).validate(jsonData)
            #Draft7Validator(jsonSchema).validate(jsonData)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def validate_label_selected(jsonData):
    try:
        with open('schema/label_selected.schema') as schema: 
            jsonSchema = json.load(schema)
            validate(instance=jsonData, schema=jsonSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def validate_sleep_created(jsonData):
    try:
        with open('schema/sleep_created.schema') as schema: 
            jsonSchema = json.load(schema)
            validate(instance=jsonData, schema=jsonSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def validate_workout_created(jsonData):
    try:
        with open('schema/workout_created.schema') as schema: 
            jsonSchema = json.load(schema)
            validate(jsonData, jsonSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

if __name__ == '__main__':
    path = 'event/*.json'   
    files = glob.glob(path)
    for filename in files: 
        try:
            with open(filename) as data: 
                jsondata = json.load(data)
                print(validate_cmarker_created(jsondata))
                print(validate_label_selected(jsondata))
                print(validate_sleep_created(jsondata))
                print(validate_workout_created(jsondata))
        except IOError as exc:
            if exc.errno != errno.EISDIR: 
                raise
    

