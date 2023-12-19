import json

import requests


class BookingApp:
    def __init__(self):
        self.base_url = "https://restful-booker.herokuapp.com"

    def auth_create_token(self):
        url = f"{self.base_url}/auth"

        payload = json.dumps({
            "username": "admin",
            "password": "password123"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    def get_booking_ids(self):
        url = f"{self.base_url}/booking"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        return response

    def get_booking(self, booking_id):
        url = f"{self.base_url}/booking/{booking_id}"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        return response

    def create_booking(self):
        url = f"{self.base_url}/booking"

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
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response

    def update_booking(self, booking_id, token):
        # booking_id = self.create_booking().json()['bookingid']
        # token = self.auth_create_token().json()['token']

        url = f"{self.base_url}/booking/{booking_id}"

        payload = json.dumps({
            "firstname": "James2",
            "lastname": "Brown2",
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

        return response

    def partial_update_booking(self, booking_id, token):
        url = f"{self.base_url}/booking/{booking_id}"

        payload = json.dumps({
            "firstname": "James3",
            "lastname": "Brown3"
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Cookie': f'token={token}'
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)

        return response

    def delete_booking(self, booking_id, token):
        url = f"{self.base_url}/booking/{booking_id}"

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Cookie': f'token={token}'
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)

        return response

    def ping_health_check(self):
        url = f"{self.base_url}/ping"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        return response
