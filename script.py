import json
import jsonschema
from jsonschema import validate, Draft6Validator, Draft7Validator
import glob
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)


def validate_schemas():
    path = 'schema/*.schema'   
    files = glob.glob(path)
    for filename in files: 
        try:
            with open(filename) as data: 
                jsonschema = json.load(data)
                Draft7Validator.check_schema(jsonschema)
                print(filename + ' scheme validation successful')
        except jsonschema.exceptions.ValidationError as err:
            print(err.message)
            return False
        except IOError as exc:
            if exc.errno != errno.EISDIR: 
                raise
    return True


def validate_cmarker_created(jsonData):
    try:
        with open('schema/cmarker_created.schema') as schema: 
            jsonSchema = json.load(schema)
            Draft7Validator(jsonSchema).validate(jsonData)
    except jsonschema.exceptions.ValidationError as err:
        print(err.message)
        return False
    return True

def validate_label_selected(jsonData):
    try:
        with open('schema/label_selected.schema') as schema: 
            jsonSchema = json.load(schema)
            Draft7Validator(jsonSchema).validate(jsonData)
    except jsonschema.exceptions.ValidationError as err:
        print(err.message)
        return False
    return True

def validate_sleep_created(jsonData):
    try:
        with open('schema/sleep_created.schema') as schema: 
            jsonSchema = json.load(schema)
            Draft7Validator(jsonSchema).validate(jsonData)
    except jsonschema.exceptions.ValidationError as err:
        print(err.message)
        return False
    return True

def validate_workout_created(jsonData):
    try:
        with open('schema/workout_created.schema') as schema: 
            jsonSchema = json.load(schema)
            Draft7Validator(jsonSchema).validate(jsonData)
    except jsonschema.exceptions.ValidationError as err:
        print(err.message)
        return False
    return True

if __name__ == '__main__':
    # validating schemas
    print('Check if schemas are valid.........')
    if validate_schemas():
        print('...all schemas are valid')
        logging.info("Given schemas are valid")
    else: 
        print('...schemas invalid')
        logging.error("Given schemas are invalid")

    
    # validating json with schemas    
    path = 'event/*.json'   
    files = glob.glob(path)
    for filename in files: 
        try:
            with open(filename) as data: 
                jsondata = json.load(data)
                validate_cmarker_created(jsondata)
                validate_label_selected(jsondata)
                validate_sleep_created(jsondata)
                validate_workout_created(jsondata)
        except IOError as exc:
            if exc.errno != errno.EISDIR: 
                raise
    

