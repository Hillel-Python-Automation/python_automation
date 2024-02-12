import requests
# POST (Authorization)
url = "https://restful-booker.herokuapp.com/auth"
result = requests.post(url)
json_for_authorization = {
    "username" : "admin",
    "password" : "password123"
}
if result.status_code == 200:
    result_data = result.json()
    print(result_data)
else:
    print(f"Error: {result.status_code}")
# GET (Get All Booked Slots)
url = "https://restful-booker.herokuapp.com/booking"
result = requests.get(url)
json_for_get_all = {
"username" : "admin",
"password" : "password123"
}
if result.status_code == 200:
    result_data = result.json()
    print(result_data)
else:
    print(f"Error: {result.status_code}")
# POST. Booking creation

import requests

url = "https://restful-booker.herokuapp.com/booking"

json_for_creation = {
    "firstname": "Arnold",
    "lastname": "Winter",
    "totalprice": 124,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

try:
    response = requests.post(url, json=json_for_creation)
    response.raise_for_status()
    if response.headers.get("Content-Type"):
        if "json" in response.headers.get("Content-Type"):
            result_data = response.json()
            print(result_data)
        else:
            print("Response is not JSON:", response.content)
    else:
        print("Content-Type header not found in response.")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
#Patch
url = "https://restful-booker.herokuapp.com/booking/1430"
json_for_updating = {
    "firstname" : "Leya",
    "lastname" : "Organa"

}
if result.status_code == 200:
    result_data = result.json()
    print(result_data)
else:
    print(f"Error: {result.status_code}")
#Delete record

url = "https://restful-booker.herokuapp.com/booking/464"
result = requests.delete(url)
if result.status_code == 200:
    result_data = result.json()
    print(result_data)
else:
    print(f"Error: {result.status_code}")