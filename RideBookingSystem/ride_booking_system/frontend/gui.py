# frontend/gui.py
import tkinter as tk
from tkinter import messagebox
from ..backend.booking_manager import BookingManager
from ..backend.vehicle import Car, Van, Bike
from ..backend.booking import Booking

class RideBookingGUI:
	def __init__(self, master):
		self.master = master
		master.title("Ride Booking System")
		self.manager = BookingManager()
		self.booking_id_counter = max([b.booking_id for b in self.manager.bookings], default=0) + 1

		# Labels and Entries for Booking a Ride
		tk.Label(master, text="User:").grid(row=0, column=0)
		self.entry_user = tk.Entry(master)
		self.entry_user.grid(row=0, column=1)

		tk.Label(master, text="Vehicle:").grid(row=1, column=0)
		self.vehicle_var = tk.StringVar(value="Car")
		tk.OptionMenu(master, self.vehicle_var, "Car", "Van", "Bike").grid(row=1, column=1)

		tk.Label(master, text="Start Location:").grid(row=2, column=0)
		self.entry_start = tk.Entry(master)
		self.entry_start.grid(row=2, column=1)

		tk.Label(master, text="End Location:").grid(row=3, column=0)
		self.entry_end = tk.Entry(master)
		self.entry_end.grid(row=3, column=1)

		tk.Label(master, text="Distance:").grid(row=4, column=0)
		self.entry_distance = tk.Entry(master)
		self.entry_distance.grid(row=4, column=1)

		# Buttons for Actions
		tk.Button(master, text="Book Ride", command=self.book_ride).grid(row=5, column=0, pady=5)
		tk.Button(master, text="View All Bookings", command=self.view_bookings).grid(row=5, column=1, pady=5)

		# Labels and Entry for Cancelling a Booking
		tk.Label(master, text="Cancel Booking ID:").grid(row=6, column=0)
		self.entry_cancel = tk.Entry(master)
		self.entry_cancel.grid(row=6, column=1)
		tk.Button(master, text="Cancel Booking", command=self.cancel_booking).grid(row=7, column=0, columnspan=2, pady=5)

		# Text Display for Bookings
		self.text_display = tk.Text(master, height=10, width=50)
		self.text_display.grid(row=8, column=0, columnspan=2)

	def book_ride(self):
		user = self.entry_user.get()
		vehicle_type = self.vehicle_var.get()
		start = self.entry_start.get()
		end = self.entry_end.get()
		try:
			distance = float(self.entry_distance.get())
		except ValueError:
			messagebox.showerror("Error", "Distance must be a number.")
			return

		if vehicle_type == "Car":
			vehicle = Car("Car", 10, 4)
		elif vehicle_type == "Van":
			vehicle = Van("Van", 8, 6)
		else:
			vehicle = Bike("Bike", 5, 1)

		booking = Booking(self.booking_id_counter, user, vehicle, start, end, distance)
		self.manager.add_booking(booking)
		messagebox.showinfo("Success", f"Ride booked! ID: {self.booking_id_counter}")
		self.booking_id_counter += 1
		self.view_bookings()  # Refresh the displayed bookings

	def view_bookings(self):
		bookings = self.manager.view_all_bookings()
		self.text_display.delete(1.0, tk.END)
		for b in bookings:
			self.text_display.insert(tk.END, b + "\n")

	def cancel_booking(self):
		booking_id_str = self.entry_cancel.get()
		if booking_id_str.isdigit():
			booking_id = int(booking_id_str)
			self.manager.cancel_booking(booking_id)
			messagebox.showinfo("Cancelled", f"Booking ID {booking_id} cancelled.")
		else:
			messagebox.showerror("Error", "Please enter a valid Booking ID.")
		self.view_bookings()  # Refresh the displayed bookings
