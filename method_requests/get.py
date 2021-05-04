import requests
import json


def request_get(url):
    try:
        response = requests.get(url)
        print(f"The request was to: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: \n {json.dumps(response.json(), indent=4)}")
        return
    except requests.exceptions.RequestException as e:
        raise e


def request_get_with_params(url, params):
    try:
        response = requests.get(url, params=json.loads(params))
        print(f"The request was to: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: \n {json.dumps(response.json(), indent=4)}")
        print(f"Params: {response.url}")
        return
    except requests.exceptions.RequestException as e:
        raise e


def request_get_with_headers():
    pass


def request_get_with_headers_params():
    # TODO: create method
    pass
