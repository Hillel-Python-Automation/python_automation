from _pytest.fixtures import fixture

from lesson_20.home_work.iegorkobieliev.booking_app import BookingApp


@fixture
def auth_create_token():
    return BookingApp().auth_create_token()


@fixture
def get_booking_ids():
    return BookingApp().get_booking_ids()


@fixture
def create_booking():
    app = BookingApp()
    response = app.create_booking()
    yield response
    booking_id = response.json()['bookingid']
    token = app.auth_create_token().json()['token']
    BookingApp().delete_booking(booking_id=booking_id, token=token)
