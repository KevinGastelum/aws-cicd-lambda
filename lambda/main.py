import os
from dotenv import load_dotenv
load_dotenv()

def handler(event, context):
    version = os.environ.get('VERSION', '0.0')
    response_body = {'message': 'Hello World', 'version': version}
    return {"statusCode": 200, "body": response_body}

# print(os.environ.get("VERSION"))
