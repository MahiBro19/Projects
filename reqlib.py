import requests
response=requests.get("https://bmwofnewton.com")
print(response.status_code)

# Method 1
'''
if response.status_code == 200:
    print("Successful")
elif response.status_code == 404 : 
    print("Unsuccessful")
'''

# Method 2
'''
if response:
    print("Successful")
else:
    raise Exception(f"Unsuccessful {response.status_code}")
'''

#Full
import requests
from requests.exceptions import HTTPError

URLS = ["https://api.github.com", "https://api.github.com/invalid"]

for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success!")
