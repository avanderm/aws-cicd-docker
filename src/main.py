import json
import jsonschema

def handler(event, context):
    with open('schema.json') as f:
        schema = json.load(f)

    jsonschema.validate(event, schema)
