from flask import Flask, Response, request
import util

app = Flask(__name__)
endpoints = None


@app.route('/<path:path>', methods=['GET', 'DELETE', 'POST', 'PUT'])
def process_request(path):
    print("Received request for path :", path, " method : ", request.method)
    error = validate_request(path, request.method)
    if error:
        print(error)
        return Response(response=error, status=500)
    resp = endpoints.lookup(path)
    return Response(response=resp.response_body, status=resp.status_code)


def validate_request(path, method):
    error = None
    if not endpoints:
        error = "missing endpoint in rest_endpoints.json"
    if not endpoints.lookup(path):
        error = "missing path in rest_endpoints.json"

    endpoint = endpoints.lookup(path)
    if endpoint and method != endpoint.method:
        error = "mismatch in method for endpoint"
    return error


host, port, endpoints = util.read_json()
app.run(host=host, port=port)

