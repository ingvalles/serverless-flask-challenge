# Use this code snippet in your app.
# If you need more information about configurations or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developers/getting-started/python/

import os
import json


def get_secret():
    # Check if the json exists
    print(os.environ.get('SERVICE_STAGE'))
    if os.environ.get('SERVICE_STAGE') == 'local' and os.path.exists('config/secrets.json'):
        # Check if the file is older than 1 hour
         with open('config/secrets.json') as json_file:
            return json.load(json_file)
