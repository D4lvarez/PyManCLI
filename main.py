import click
import requests
import json

# TODO: Refactor code
from method_requests.get import request_get, request_get_with_params


def make_request(url, mode, params, body, headers):
    if mode.lower() == 'post':
        if len(body) == 0:
            raise Exception("--body param it's required for post, put and delete methods")
        if len(headers) != 0:
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
        try:
            response = requests.post(url, data=json.loads(body))
            print(f"The request was to: {url}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: \n {json.dumps(response.json(), indent=4)}")
            print(f"Params: {response.url}")
            return
        except requests.exceptions.RequestException as e:
            raise e

    elif mode.lower() == 'delete':
        if len(headers) != 0:
            try:
                response = requests.delete(url, headers=eval(headers))
                print(f"The request was to: {url}")
                print(f"Request Headers: \n {response.request.headers}")
                print(f"Status Code: {response.status_code}")
                print(f"Response Body: \n {json.dumps(response.json(), indent=4)}")
                print(f"Params: {response.url}")
                return
            except requests.exceptions.RequestException as e:
                raise e
        try:
            response = requests.delete(url)
            print(f"The request was to: {url}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: \n {json.dumps(response.json(), indent=4)}")
            print(f"Params: {response.url}")
            return
        except requests.exceptions.RequestException as e:
            raise e

    elif mode == 'put':
        if len(headers) != 0:
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
        try:
            response = requests.put(url)
            print(f"The request was to: {url}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: \n {json.dumps(response.json(), indent=4)}")
            print(f"Params: {response.url}")
            return
        except requests.exceptions.RequestException as e:
            raise e

    elif mode.lower() == 'get':
        if len(params) != 0:
            request_get_with_params(url, params)
        request_get(url)
    else:
        raise Exception("This method its not allowed")


@click.command()
@click.option('--url', default='http://localhost:8000', help="Set the URL target")
@click.option('--mode', default='get', help="Set the mode of request")
@click.option('--params', default={}, help="Set the params to Get Request. Most be in JSON format.")
@click.option('--body', default={}, help="Set the body form data to Post Request. Most be in JSON format.")
@click.option('--headers', default={}, help='Set the headers to make a request. Most be in JSON format')
def cli(url, mode, params, body, headers):
    make_request(url=url, mode=mode, params=params, body=body, headers=headers)


if __name__ == '__main__':
    cli()
