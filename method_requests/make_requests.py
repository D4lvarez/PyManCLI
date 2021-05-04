from method_requests.delete import request_delete_with_headers, request_delete
from method_requests.get import request_get, request_get_with_params
from method_requests.post import request_post_with_headers, request_post
from method_requests.put import request_put, request_put_with_headers


def make_request(url, mode, params, body, headers):
    """
    Performs a request according to the method passed by the argument mode
    :param url: string
    :param mode: string
    :param params: string
    :param body: string
    :param headers: string
    :return: void
    """
    if mode.lower() == 'post':
        if len(body) == 0:
            raise Exception("--body param it's required for post, put and delete methods")
        if len(headers) != 0:
            request_post_with_headers(url, body, headers)
        request_post(url, body)
    elif mode.lower() == 'delete':
        if len(headers) != 0:
            request_delete_with_headers(url, headers)
        request_delete(url)
    elif mode == 'put':
        if len(headers) != 0:
            request_put_with_headers(url, headers)
        request_put(url)
    elif mode.lower() == 'get':
        if len(params) != 0:
            request_get_with_params(url, params)
        request_get(url)
    else:
        raise Exception("This method its not allowed")
