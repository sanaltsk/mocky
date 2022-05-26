from endpoint import Endpoint


class Endpoints:
    """
        The __init__ function is called when a new object is created.
        It initializes the attributes of the class, and it can take arguments
        when called. In this case, we are passing in an array of dictionaries that
        contain information about each endpoint.

        :param self: Refer to the object that is being created
        :param endpoints: Define the endpoints that will be used in the test
        :return: The object that is created when the class is called
    """
    endpoints_dict = {}

    def __init__(self, endpoints):
        for endpoint in endpoints:
            endpoint_object = Endpoint(endpoint['endpoint'],
                                       endpoint['method'],
                                       endpoint['response']['status_code'],
                                       endpoint['response']['response_body'])
            self.endpoints_dict[endpoint_object.path] = endpoint_object

    def lookup(self, endpoint_path):
        """
        The lookup function is responsible for taking a path and returning the
        associated value.  For example, if you have a dictionary like this:

            {'a': 1, 'b': 2}

        Then you can use `lookup('a')` to get back 1.  Or `lookup('c')` to get back None.


        :param self: Reference the class instance
        :param endpoint_path: Specify the path to a particular endpoint
        :return: A list of dictionaries
        """
        return self.endpoints_dict[endpoint_path] if endpoint_path in self.endpoints_dict else None
