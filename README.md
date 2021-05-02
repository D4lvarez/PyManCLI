# PyManCLI
## _A CLI made it on Python to test APIs_

It arose out of the need to test my own projects without installing other software for the same purpose.

## Status
- At the moment only GET requests with and without parameters are made.
- Other requests in development

## Implemented packages
- [click](https://click.palletsprojects.com/en/7.x/)
- [requests](https://docs.python-requests.org/en/latest/user/install/#install)

> The click package allows to generate the cli in a simple way by using decorators
> the requests package is implemented to make the requests and get the responses for each request

## How to use

After installing the necessary packages, the ```main.py``` file is executed by passing the following arguments to it:

- --url: E.g: ```--url http://localhost:8000``` (default url).
- --params: They must be in quotes and in JSON format. E.g: ```--params '{"key":"value"}'```

The execution would look like this: ```python main.py --url http://localhost:8000 --params '{"key":"value"}'```

## License

AGL

**Free Software, Hell Yeah!**
__The name is just Py (python) Man (Postman) CLI (CLI) saturday night ideas__
### More Features Incoming
