import requests
import json

# authorisation
print("*" * 5, "create a token", "*" * 5)
payload = {
    "username" : "admin",
    "password" : "password123"
}

r = requests.post("https://restful-booker.herokuapp.com/auth", data=payload)
auth_resp = r.json()
token = auth_resp["token"]
print(token)
print()

# create (post)
print("*" * 5, "post", "*" * 5)
payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}
cookie = {
    "token": token,
}

r = requests.post("https://restful-booker.herokuapp.com/booking", data=json.dumps(payload), headers=headers)
booking = r.json()
id = booking["bookingid"]
print(booking)
print()


 # get
print("*" * 5, "get", "*" * 5)
r = requests.get(f"https://restful-booker.herokuapp.com/booking/{id}")
print(r.json())
print()

#  put
print("*" * 5, "put", "*" * 5)

payload = {
    "firstname" : "James new",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Cookie": f"token={token}",
    # "Authorisation": "Basic YWRtaW46cGFzc3dvcmQxMjM=",

}
r = requests.put(f"https://restful-booker.herokuapp.com/booking/{id}", data=json.dumps(payload), headers=headers)
print(r.json())


# delete
print("*" * 5, "delete", "*" * 5)
headers = {
    "Cookie": f"token={token}",
}

r = requests.delete(f"https://restful-booker.herokuapp.com/booking/{id}", headers=headers)
print('delete status code:', r.status_code)