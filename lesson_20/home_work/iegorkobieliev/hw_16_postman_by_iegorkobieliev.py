import json

from lesson_20.home_work.iegorkobieliev.booking_app import BookingApp

app = BookingApp()


def test_0_auth_create_token(auth_create_token):
    response = auth_create_token

    print(json.dumps(response.json(), indent=2))
    assert response.status_code == 200


def test_1_get_bookings(get_booking_ids):
    response = get_booking_ids

    print(json.dumps(response.json(), indent=2))
    assert response.status_code == 200


def test_2_get_booking(create_booking):
    booking_id = create_booking.json()['bookingid']

    response = app.get_booking(booking_id=booking_id)

    print(json.dumps(response.json(), indent=2))
    assert response.status_code == 200


def test_3_create_booking(create_booking):
    response = create_booking

    print(json.dumps(response.json(), indent=2))
    assert response.status_code == 200
    assert response.json()['bookingid'] > 0


def test_4_update_booking(create_booking, auth_create_token):
    booking_id = create_booking.json()['bookingid']
    token = auth_create_token.json()['token']

    response = app.update_booking(booking_id=booking_id, token=token)

    print(json.dumps(response.json(), indent=2))
    assert response.status_code == 200


def test_5_partial_update_booking(create_booking, auth_create_token):
    booking_id = create_booking.json()['bookingid']
    token = auth_create_token.json()['token']

    response = app.partial_update_booking(booking_id=booking_id, token=token)

    print(json.dumps(response.json(), indent=2))
    assert response.status_code == 200


def test_6_delete_booking(create_booking, auth_create_token):
    booking_id = create_booking.json()['bookingid']
    token = auth_create_token.json()['token']

    response = app.delete_booking(booking_id=booking_id, token=token)

    print(booking_id)
    print(response.text)
    assert response.status_code == 201
    assert response.text == "Created"
    assert app.get_booking(booking_id=booking_id).status_code == 404


def test_7_ping_health_check():
    response = app.ping_health_check()

    print(response.text)
    assert response.status_code == 201
    assert response.text == "Created"
