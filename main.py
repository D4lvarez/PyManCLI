import click
import requests
import json


def make_request(url, mode, params, form, headers):
    if mode == 'post':
        pass
    elif mode == 'delete':
        pass
    elif mode == 'put':
        pass
    elif mode == 'get':
        if len(params) != 0:
            try:
                response = requests.get(url, params=params)
                print(f"The request was to: {url}")
                print(f"Status Code: {response.status_code}")
                print(f"Response Body: \n {json.dumps(response.json(), indent=4)}")
                print(f"Params: {response.url}")
                return
            except requests.exceptions.RequestException as e:
                raise e
        try:
            response = requests.get(url)
            print(f"The request was to: {url}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: \n {json.dumps(response.json(), indent=4)}")
            return
        except requests.exceptions.RequestException as e:
            raise e
    else:
        ValueError()


@click.command()
@click.option('--url', default='http://localhost:8000', help="Set the URL target")
@click.option('--mode', default='get', help="Set the mode of request")
@click.option('--params', default={}, help="Set the params to Get Request. Most be in JSON format.")
@click.option('--form', default={}, help="Set the body form data to Post Request. Most be in JSON format.")
@click.option('--headers', default={}, help='Set the headers to make a request. Most be in JSON format')
def cli(url, mode, params, form, headers):
    make_request(url, mode.lower(), json.loads(params), form, headers)


if __name__ == '__main__':
    cli()
