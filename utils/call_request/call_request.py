import json
import requests


class CallRequest:
    def __init__(self):
        self.api_token = "abb0ea8df57b069ec4d85939e14b5913"
        self.headers = {
            'X-TrackerToken': self.api_token,
            'Content-Type': 'application/json'
        }

    def _send_request(self, method, url, headers=None, payload=None):
        if headers is None:
            headers = self.headers

        if payload is not None:
            payload = json.dumps(payload)

        response = requests.request(method, url, headers=headers, data=payload)

        return response

    def post(self, url="", headers=None, payload=None):
        return self._send_request("POST", url, headers, payload)

    def get(self, url="", headers=None, payload=None):
        return self._send_request("GET", url, headers, payload)

    def delete(self, url="", headers=None, payload=None):
        return self._send_request("DELETE", url, headers, payload)

