import click

from method_requests.make_requests import make_request


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
