import requests
import json

print('1.Ex. Auth - CreateToken')

url = "https://restful-booker.herokuapp.com/auth"

payload = json.dumps({
  "username": "admin",
  "password": "password123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

print(50 * '*')

print('2.Ex. GetBookingIds ')

url = "https://restful-booker.herokuapp.com/booking"

payload = json.dumps({
  "username": "admin",
  "password": "password123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

bookingID = response.json()[0]['bookingid']

print(response.text)

print(50 * '*')

print('3.Ex. GetBooking')

url = f"https://restful-booker.herokuapp.com/booking/{bookingID}"

payload = json.dumps({
#  "username": "admin",
#  "password": "password123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)



print(response.text)

print(50 * '*')

print('4.Ex. CreateBooking')

url = "https://restful-booker.herokuapp.com/booking"

payload = json.dumps({
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

print(50 * '*')

print('5.Ex.UpdateBooking')

url = f"https://restful-booker.herokuapp.com/booking/{bookingID}"

payload = json.dumps({
    "firstname" : "James",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Cookie': 'token=<token_value>',
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

print(50 * '*')

print('6.Ex.PartialUpdateBooking')

url = f"https://restful-booker.herokuapp.com/booking/{bookingID}"

payload = json.dumps({
    "firstname": "James",
    "lastname": "Brown"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Cookie': 'token=<token_value>',
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)

print(50 * '*')

print('7.Ex.DeleteBooking')
url = f"https://restful-booker.herokuapp.com/booking/1?id={bookingID}"
payload = {}
headers = {

  'Cookie': 'token=<token_value>',
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
}
response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)