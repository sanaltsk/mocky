class Endpoint:
    path = None
    method = None
    status_code = None
    response_body = None

    def __init__(self, path, method, status_code, response_body):
        self.path = path
        self.method = method
        self.status_code = status_code
        self.response_body = response_body
