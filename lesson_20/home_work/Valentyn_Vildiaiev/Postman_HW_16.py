import requests
import json
print("POST: " + "Auth - CreateToken")
url = "https://restful-booker.herokuapp.com/auth"

payload = json.dumps({
  "username": "admin",
  "password": "password123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
token = response.json()["token"]
print(response.text)
print("Today our token is: " + token)
print("*" * 50)

print("GET: " + "Booking - GetBookingIds")
url = "https://restful-booker.herokuapp.com/booking"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print("*" * 50)

print("POST: " + "Booking - CreateBooking")
url = "https://restful-booker.herokuapp.com/booking"

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

response = requests.request("POST", url, headers=headers, data=payload)
bookID = response.json()["bookingid"]
print("The bookID is: " + str(bookID))
print(response.text)
print("*" * 50)

print("PUT: " + "Booking - UpdateBooking")
url = f'https://restful-booker.herokuapp.com/booking/{bookID}'

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
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Cookie': f'token={token}'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
print("*" * 50)

print("PATCH: " + "Booking - PartialUpdateBooking")
url = f'https://restful-booker.herokuapp.com/booking/{bookID}'

payload = json.dumps({
  "firstname": "James",
  "lastname": "Brown"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Cookie': f'token={token}'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
print("*" * 50)

print("DELETE: " + "Booking - DeleteBooking")

url = f'https://restful-booker.herokuapp.com/booking/{bookID}'

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Cookie': f'token={token}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
