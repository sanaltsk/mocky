import json
from flask import Flask, Response, request

import util

app = Flask(__name__)
ENDPOINTS = None


@app.route('/<path:path>', methods=['GET', 'DELETE', 'POST', 'PUT'])
def process_request(path):
    """
    The process_request function is the main entry point for the API. It is responsible for
    validating that a request is valid and then dispatching it to the appropriate endpoint function.


    :param path: Determine the endpoint to be called
    :return: The response to the request
    """
    print("Received request for path :", path, " method : ", request.method)
    error = validate_request(path, request.method)
    if error:
        print(error)
        return Response(response=error, status=500)
    resp = ENDPOINTS.lookup(path)
    body = json.dumps(resp.response_body) if type(resp.response_body) \
                                             in [dict, list] else str(resp.response_body)
    return Response(response=body, status=resp.status_code)


def validate_request(path, method):
    """
    The validate_request function checks to see if the request is valid.
    It checks to make sure that the path exists in rest_endpoints.json and that the method
    matches what's listed in rest_endpoints.json.

    :param path: Determine which endpoint is being called
    :param method: Check if the method is valid
    :return: An error if the path and method do not match up with an endpoint
    """
    error = None
    if not ENDPOINTS:
        error = "missing endpoint in rest_endpoints.json"
    if not ENDPOINTS.lookup(path):
        error = "missing path in rest_endpoints.json"

    endpoint = ENDPOINTS.lookup(path)
    if endpoint and method != endpoint.method:
        error = "mismatch in method for endpoint"
    return error


# Reading the json file and assigning the host, port, and ENDPOINTS to the variables.
host, port, ENDPOINTS = util.read_json()
app.run(host=host, port=port)
