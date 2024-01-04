from lesson_20.home_work.iegorkobieliev.booking_app import BookingApp


# 1. Використайте один з попередньо створених класів
class BookingAppPrinter(BookingApp):
    __counter: int = 0

    def __init__(self):
        super().__init__()
        BookingAppPrinter.__counter += 1

    def __del__(self):
        del self
        BookingAppPrinter.__counter -= 1

    # 2. Додайте до нього методи @classmethod i @staticmethod
    @classmethod
    def print_booking_ids_status_code(cls):
        print(f"Status code: {cls().get_booking_ids().status_code}")

    @staticmethod
    def print_number_of_instances():
        print(f"Amount of instances: {BookingAppPrinter.__counter}")


print("_" * 30)
bap1 = BookingAppPrinter()
bap1.print_booking_ids_status_code()

BookingAppPrinter.print_number_of_instances()

bap_list = []
for i in range(3):
    bap_list.append(BookingAppPrinter())

BookingAppPrinter.print_number_of_instances()

del bap1
BookingAppPrinter.print_number_of_instances()
