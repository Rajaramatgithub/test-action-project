#!/usr/bin/env python
import json
import requests
import os

message = 'My first automated slack post'
 
def post_to_slack(message):
    data = {'text':message}
    url = os.environ["SLACK_WEBHOOK_TEST_CHANNEL"]
    requests.post(url,json=data, verify=False)
 
 
if __name__ == '__main__':
    post_to_slack(message)
