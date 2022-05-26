import json
import contants
from endpoints import Endpoints


def read_json():
    """
    The read_json function reads the input JSON file and creates an Endpoints object.
    The endpoints_list is a list of all the endpoints in the JSON file.

    :return: A list of endpoints objects
    """
    with open(contants.INPUT_JSON_FILE, encoding="utf-8") as file:
        json_input = json.load(file)
        endpoints_list = Endpoints(json_input['endpoints'])
    return json_input['hostname'], json_input['port'], endpoints_list
