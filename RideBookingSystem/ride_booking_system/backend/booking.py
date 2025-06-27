# backend/booking.py
class Booking:
	def __init__(self, booking_id, user, vehicle, start_location,
				 end_location, distance):
		self.booking_id = booking_id
		self.user = user
		self.vehicle = vehicle
		self.start_location = start_location
		self.end_location = end_location
		self.distance = distance
		self.total_cost = vehicle.calculate_cost(distance)

	def to_dict(self):
		return {
			"booking_id": self.booking_id,
			"user": self.user,
			"vehicle": {
				"vehicle_type": self.vehicle.vehicle_type,
				"cost_per_mile": self.vehicle.cost_per_mile,
				"capacity": self.vehicle.capacity
			},
			"start_location": self.start_location,
			"end_location": self.end_location,
			"distance": self.distance,
			"total_cost": self.total_cost
		}

	def __str__(self):
		return (f"ID: {self.booking_id}, User: {self.user}, Vehicle: "
				f"{self.vehicle.vehicle_type}, "
				f"From: {self.start_location} To: {self.end_location}, "
				f"Distance: {self.distance}, Cost: {self.total_cost}")
