import requests
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from datetime import datetime

class AddSavingsPopup(tk.Frame):
    """ Popup Frame to Add an Savings Account """

    def __init__(self, parent, close_callback):
        """ Constructor """
        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        ttk.Label(self, text="First Name:").grid(row=2, column=1, sticky=W)
        self._fname = ttk.Entry(self)
        self._fname.grid(row=2, column=2)
        ttk.Label(self, text="Last Name:").grid(row=3, column=1, sticky=W)
        self._lname = ttk.Entry(self)
        self._lname.grid(row=3, column=2)
        ttk.Label(self, text="Interest:").grid(row=4, column=1, sticky=W)
        self._interest = ttk.Entry(self)
        self._interest.grid(row=4, column=2)
        ttk.Label(self, text="Date Interest:").grid(row=5, column=1, sticky=W)
        self._date_interest = ttk.Entry(self)
        self._date_interest.grid(row=5, column=2)

        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=6, column=1)
        ttk.Button(self, text="Close", command=self._close_cb).grid(row=6, column=2)

    def _submit_cb(self):
        """ Submit the Add Savings Account"""
        data = {}
        data['fname'] = self._fname.get()
        data['lname'] = self._lname.get()
        data['interest'] = self._interest.get()
        data['date_interest'] = self._date_interest.get()

        if data['fname'] or data['lname'] or data['interest'] or data['date_interest'] == "":
            messagebox.showerror("Error", "All slots must be filled.")
        elif not data["fname"].lower().replace(" ", "").isalpha():
            messagebox.showerror("Error", "Must be a first name with only letters.")
        elif not data["lname"].lower().replace(" ", "").isalpha():
            messagebox.showerror("Error", "Must be a last name with only letters.")
        elif not data["interest"].isdigit():
            messagebox.showerror("Error", "Must be an integer.")
        try:
            data["date_interest"] != datetime.strptime(data["date_interest"],
                                                        "%Y-%m-%d").strftime('%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Must be in YYYY-MM-DD format")
        else:
            messagebox.showinfo("Success", "Savings Account is added. Please close the popups.")
            requests.post(f"http://127.0.0.1:5000/bank/savings", json=data)


