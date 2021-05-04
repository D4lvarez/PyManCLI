# PyManCLI
## _A CLI made it on Python to test APIs_

It arose out of the need to test my own projects without installing other software for the same purpose.

## Status
- Allowed methods GET, POST, PUT and DELETE.
- Working on add custom params to PUT and DELETE methods.

## Implemented packages
- [click](https://click.palletsprojects.com/en/7.x/)
- [requests](https://docs.python-requests.org/en/latest/user/install/#install)
- [json](https://docs.python.org/3/library/json.html)

> The click package allows to generate the cli in a simple way by using decorators
> the requests package is implemented to make the requests and get the responses for each request

## How to use

### Method Get
The method get is assigned by default.
After installing the necessary packages, the ```main.py``` file is executed by passing the following arguments to it:

- --url: E.g: ```--url http://localhost:8000``` (default url).
- --params (optional): They must be in quotes and in JSON format. E.g: ```--params '{"key":"value"}'```

The execution would look like this: ```python main.py --url http://localhost:8000 --params '{"key":"value"}'```

### Method Post
After installing the necessary packages, the ```main.py``` file is executed by passing the following arguments to it:

- --url: E.g: ```--url http://localhost:8000``` (default url).
- --mode (required): The mode method, in this case "post". E.g: ```--mode post```
- --body (required): They must be in quotes and in JSON format. E.g: ```--body '{"key":"value"}'```
- --headers (optional): They must be in quotes and in JSON format. E.g: ```--headers '{"key":"value"}'```

The execution would look like this: ```python main.py --url http://localhost:8000 --mode post --body '{"key":"value"}' --headers '{"key":"value"}'```

### Method Put
After installing the necessary packages, the ```main.py``` file is executed by passing the following arguments to it:

- --url: E.g: ```--url http://localhost:8000``` (default url).
- --mode (required): The mode method, in this case "put". E.g: ```--mode put```
- --headers (optional): They must be in quotes and in JSON format. E.g: ```--headers '{"key":"value"}'```

The execution would look like this: ```python main.py --url http://localhost:8000 --mode put --headers '{"key":"value"}'```

### Method Delete
After installing the necessary packages, the ```main.py``` file is executed by passing the following arguments to it:

- --url: E.g: ```--url http://localhost:8000``` (default url).
- --mode (required): The mode method, in this case "delete". E.g: ```--mode delete```
- --headers (optional): They must be in quotes and in JSON format. E.g: ```--headers '{"key":"value"}'```

The execution would look like this: ```python main.py --url http://localhost:8000 --mode delete --headers '{"key":"value"}'```


## License

AGPL

**Free Software, Hell Yeah!**
__The name is just Py (python) Man (Postman) CLI (CLI). Saturday night ideas__
### More Features Incoming
