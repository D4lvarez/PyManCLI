import requests
import json


def request_put(url):
    try:
        response = requests.put(url)
        print(f"The request was to: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: \n {json.dumps(response.json(), indent=4)}")
        print(f"Params: {response.url}")
        return
    except requests.exceptions.RequestException as e:
        raise e


def request_put_with_headers(url, headers):
    try:
        response = requests.put(url, headers=eval(headers))
        print(f"The request was to: {url}")
        print(f"Request Headers: \n {response.request.headers}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: \n {response}")
        print(f"Params: {response.url}")
        return
    except requests.exceptions.RequestException as e:
        raise e


def request_put_with_params(url, params):
    # TODO: create method
    pass


def request_put_with_headers_params(url, params, headers):
    # TODO: # TODO: create method
    pass
