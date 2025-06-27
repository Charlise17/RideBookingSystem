# backend/vehicle.py
class Vehicle:
	def __init__(self, vehicle_type, cost_per_mile, capacity):
		self.vehicle_type = vehicle_type
		self.cost_per_mile = cost_per_mile
		self.capacity = capacity

	def calculate_cost(self, distance):
		return self.cost_per_mile * distance

class Car(Vehicle):
	def calculate_cost(self, distance):
		return super().calculate_cost(distance) * 1.1  # luxury tax

class Van(Vehicle):
	def calculate_cost(self, distance):
		return super().calculate_cost(distance) * 0.95  # fuel discount

class Bike(Vehicle):
	def calculate_cost(self, distance):
		return super().calculate_cost(distance)
