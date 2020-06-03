import json
import os

import boto3
import jsonschema

with open('schema.json') as f:
    SCHEMA = json.load(f)

def check(event):
    jsonschema.validate(event, SCHEMA)

if __name__ == '__main__':
    sqs = boto3.resource('sqs')
    queue = sqs.Queue(os.getenv('QUEUE_URL'))

    print("Starting consumer")

    # while True:
    for message in queue.receive_messages(WaitTimeSeconds=10):
        try:
            check(json.loads(message))
            print('Valid')
        except jsonschema.ValidationError:
            print('Not valid')

        message.delete()

    print("Moving on")
