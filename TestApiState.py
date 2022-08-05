import requests
from requests.exceptions import HTTPError
import json

for url in ['http://localhost:5413/api/state']:
    try:
        result = requests.get(url)
        
        result.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!', result.json())
