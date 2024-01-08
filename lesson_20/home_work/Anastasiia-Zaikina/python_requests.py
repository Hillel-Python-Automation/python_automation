import requests
import json

print(20*'-')
print('Create Auth Token')

url = "https://restful-booker.herokuapp.com/auth"

payload = json.dumps({
  "username": "admin",
  "password": "password123"
})
headers = {
  'Content-Type': 'application/json'
}

auth_response = requests.request("POST", url, headers=headers, data=payload)

print(json.dumps(auth_response.json(), indent=1))

print(20*'-')
print('Get Bookings')

url = "https://restful-booker.herokuapp.com/booking"

payload = {}
headers = {}

get_response = requests.request("GET", url, headers=headers, data=payload)

print(json.dumps(get_response.json(), indent=1))

print(20*'-')
print('Post booking')

payload = json.dumps({
  "firstname": "Jim",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
})
headers = {
  'Content-Type': 'application/json'
}

post_response = requests.request("POST", url, headers=headers, data=payload)
created_post = post_response.json()
booking_id = created_post.get('bookingid')

print(json.dumps(post_response.json(), indent=1))

print(20*'-')
print('Put Booking')

url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"

payload = json.dumps({
  "firstname": "James",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
})
headers = {
  'Cookie': 'token=<0638a6db0d6c4fd>',
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
  'Content-Type': 'application/json'
}

put_response = requests.request("PUT", url, headers=headers, data=payload)

print(json.dumps(put_response.json(), indent=1))

print(20*'-')
print('Delete Booking')

url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"

payload = {}
headers = {
  'Cookie': 'token=<0638a6db0d6c4fd>',
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
}

delete_response = requests.request("DELETE", url, headers=headers, data=payload)

print(delete_response.text)