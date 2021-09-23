#!/usr/bin/env python
import json
import requests
import sys

message = 'My first automated slack post'
 
def post_to_slack(message):
    data = {'text':message}
    url = sys.argv[1]
    requests.post(url,json=data, verify=False)
 
 
if __name__ == '__main__':
    post_to_slack(message)
