import requests
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

class AddChequingsPopup(tk.Frame):
    """ Adding chequing pop up"""
    # Insert your code here
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
        ttk.Label(self, text="Fees:").grid(row=4, column=1, sticky=W)
        self._fees = ttk.Entry(self)
        self._fees.grid(row=4, column=2)
        ttk.Label(self, text="Rebate:").grid(row=5, column=1, sticky=W)
        self._rebate = ttk.Entry(self)
        self._rebate.grid(row=5, column=2)
        ttk.Label(self, text="Min Balance:").grid(row=6, column=1, sticky=W)
        self._min_balance = ttk.Entry(self)
        self._min_balance.grid(row=6, column=2)
        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=7, column=1)
        ttk.Button(self, text="Close", command=self._close_cb).grid(row=7, column=2)

    def _submit_cb(self):
        """ Submit the Add Chequings Account """
        data = {}
        data['fname'] = self._fname.get()
        data['lname'] = self._lname.get()
        data['fees'] = self._fees.get()
        data['rebate'] = self._rebate.get()
        data['min_balance'] = self._min_balance.get()

        # rebate has a default, does not need validation.
        if not data["fname"].lower().replace(" ", "").isalpha() or data['fname'] == "":
            messagebox.showerror("Error", "Must be a first name with only letters.")
        elif not data["lname"].lower().replace(" ", "").isalpha() or data['lname'] == "":
            messagebox.showerror("Error", "Must be a last name with only letters.")
        elif not data["fees"].isdigit() or data['fees'] == "":
            messagebox.showerror("Error", "Must be an integer.")
        elif not data["min_balance"].isdigit() or data['min_balance'] == "":
            messagebox.showerror("Error", "Must be an integer.")
        else:
            messagebox.showinfo("Success", "Chequings Account is added. Please close the popups.")
            requests.post("http://127.0.0.1:5000/bank/chequings", json=data)
