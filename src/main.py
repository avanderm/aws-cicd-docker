import json
import os
import time

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

    while True:
        for message in queue.receive_messages():
            try:
                check(json.loads(message))
                print('Valid')
            except jsonschema.ValidationError:
                print('Not valid')

            message.delete()

        print("Moving on")
        time.sleep(10)
