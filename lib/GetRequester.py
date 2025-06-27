import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
         # Send GET request and return the raw response content
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Send GET request and return parsed JSON (as Python list or dict)
        response = requests.get(self.url)
        return response.json()