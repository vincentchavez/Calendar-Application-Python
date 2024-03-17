# calendar_app.py

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def handle_date_selection():
    selected_date = cal.get_date()
    print("Selected date:", selected_date)

def main():
    root = tk.Tk()
    root.title("Calendar Application")

    # Create a Calendar widget
    cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=20)

    # Create a button to handle date selection
    select_button = ttk.Button(root, text="Select Date", command=handle_date_selection)
    select_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
