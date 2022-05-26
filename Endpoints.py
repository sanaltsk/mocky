from Endpoint import Endpoint


class Endpoints:
    endpoints_dict = {}

    def __init__(self, endpoints):
        for endpoint in endpoints:
            endpoint_object = Endpoint(endpoint['endpoint'],
                                       endpoint['method'],
                                       endpoint['response']['status_code'],
                                       endpoint['response']['response_body'])
            self.endpoints_dict[endpoint_object.path] = endpoint_object

    def lookup(self, endpoint_path):
        return self.endpoints_dict[endpoint_path] if endpoint_path in self.endpoints_dict else None

