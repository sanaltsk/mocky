import contants
import json
from Endpoints import Endpoints


def read_json():
    with open(contants.input_json_file) as f:
        json_input = json.load(f)
        endpoints_list = Endpoints(json_input['endpoints'])
    return json_input['hostname'], json_input['port'], endpoints_list
