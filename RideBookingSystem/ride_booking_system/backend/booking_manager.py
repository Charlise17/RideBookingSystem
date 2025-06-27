# backend/booking_manager.py
import json
from .booking import Booking
from .vehicle import Car, Van, Bike
class BookingManager:
    def __init__(self):
        self.bookings = []
        self.load_from_file()

    def add_booking(self, booking):
        self.bookings.append(booking)
        self.save_to_file()

    def cancel_booking(self, booking_id):
        self.bookings = [b for b in self.bookings if b.booking_id != booking_id]
        self.save_to_file()

    def view_all_bookings(self):
        return [str(b) for b in self.bookings]

    def save_to_file(self):
        with open("bookings.json", "w") as f:
            json.dump([b.to_dict() for b in self.bookings], f)

    def load_from_file(self):
        try:
            with open("bookings.json", "r") as f:
                bookings_data = json.load(f)
                for data in bookings_data:
                    v_type = data["vehicle"]["vehicle_type"]
                    if v_type == "Car":
                        vehicle = Car(**data["vehicle"])
                    elif v_type == "Van":
                        vehicle = Van(**data["vehicle"])
                    else:
                        vehicle = Bike(**data["vehicle"])
                    booking = Booking(
                        data["booking_id"],
                        data["user"],
                        vehicle,
                        data["start_location"],
                        data["end_location"],
                        data["distance"]
                    )
                    self.bookings.append(booking)
        except FileNotFoundError:
            self.bookings = []