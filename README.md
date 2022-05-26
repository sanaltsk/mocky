# Mocky

Mocky is a utility to mock endpoints, this can be used by developers to mock REST endpoints. Configure the endpoint and a static response to be served for the request. 
This would be helpful for 

	- Backend developers to mock request to downstream services
	- UI developers to mock backend apis until the actual apis as ready
	- Testers trying to build automation around apis that are being developed.


## Installation

Follow the below steps
	1. Clone the repo
	2. Install the utility, ` pip3 install -r requirements.txt`
	

## Run
1. Add the endpoint to be mocked in `rest_endpoints.json`

	```
	{
            "endpoint": "daily/weather",
            "method": "GET",	#GET,POST,PUT,DELETE
            "response":	
            {
                "status_code": 200,
                "response_body": "hello world"
            }
        }
	```

2. Run the server using `python app.py` or `python3 app.py` or your flavor of python command.
`python3 app.py`

## Issues
If you find/have any issues/improvements/comments, please create a GitHub issue in the repo. 

## Contribution
Feel free to improve/fix the utility.
