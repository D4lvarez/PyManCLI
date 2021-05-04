import requests
import json


def request_post(url, body):
    try:
        response = requests.post(url, data=json.loads(body))
        print(f"The request was to: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: \n {json.dumps(response.json(), indent=4)}")
        print(f"Params: {response.url}")
        return
    except requests.exceptions.RequestException as e:
        raise e


def request_post_with_headers(url, body, headers):
    try:
        response = requests.post(url, data=json.loads(body.lower()), headers=eval(headers))
        print(f"The request was to: {url}")
        print(f"Request Headers: \n {response.request.headers}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: \n {json.dumps(response.json(), indent=4)}")
        print(f"Params: {response.url}")
        return
    except requests.exceptions.RequestException as e:
        raise e
