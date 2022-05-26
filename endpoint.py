class Endpoint:
    """
        The __init__ function is called when an instance of the class is created.
        It initializes all of the attributes in our class, and it can take arguments
        when instantiating a new object. In this case, we are expecting four arguments:
        self (the name doesn't matter), path, method, and status_code.

        :param self: Refer to the object itself
        :param path: Store the path of the request
        :param method: Store the http method used for the request
        :param status_code: Store the status code of the response
        :param response_body: Store the response body of the request
        :return: The newly created object
    """
    path = None
    method = None
    status_code = None
    response_body = None

    def __init__(self, path, method, status_code, response_body):
        self.path = path
        self.method = method
        self.status_code = status_code
        self.response_body = response_body

    def __str__(self):
        return "Method: " + self.method + " Path: " + self.path + \
               ", Response: Status: " + self.status_code + \
                ", Body : " + self.response_body
