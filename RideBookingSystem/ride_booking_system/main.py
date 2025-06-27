# main.py
# ride_booking_system/main.py
import tkinter as tk
from ride_booking_system.frontend.gui import RideBookingGUI # This import is correct for running as a module

def main():
    root = tk.Tk()
    app = RideBookingGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
