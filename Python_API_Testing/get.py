import requests

base_url = "https://reqres.in/"
endpoint = "api/users?page=2"

url = base_url + endpoint

response = requests.get(url)
# print the starus code
print(response) 

# check status code

if response.status_code==200:
    print("status code is ", response.status_code)
    print(response.json())
else :
    print("error code is ",response.status_code)

