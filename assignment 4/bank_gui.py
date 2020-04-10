import tkinter as tk
import tkinter.font
from tkinter import ttk
from tkinter import *
import requests
from add_savings_popup import AddSavingsPopup
from add_chequings_popup import AddChequingsPopup
from update_savings_popup import UpdateSavingsPopup
from update_chequings_popup import UpdateChequingsPopup
from remove_account_popup import RemoveAccountPopup


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        # Left frame, column 1
        left_frame = tk.Frame(master=self, width=150, height=600,
                               bg="#C8F9C4", highlightthickness=1, highlightbackground="#111")
        left_frame.grid(row=1, column=1)
        left_frame.configure(background="SlateBlue1")

        # Center frame (info text, column 2)
        center_frame = tk.Frame(master=self, width=150, height=600,
                               bg="#C8F9C4", highlightthickness=1, highlightbackground="#111")
        center_frame.grid(row=1, column=2)
        center_frame.configure(background="SlateBlue1")

        # Right frame (info text, column 2)
        right_frame = tk.Frame(master=self, width=150, height=600,
                               bg="#C8F9C4", highlightthickness=1, highlightbackground="#111")
        right_frame.grid(row=1, column=3)
        right_frame.configure(background="SlateBlue1")

        # A couple buttons - using TTK
        ttk.Button(left_frame, text="Savings Accounts", width=18,
                   command=self._update_s_list).grid(row=7, column=1, sticky=NW, padx=5, pady=0)
        ttk.Button(left_frame, text="Chequing Accounts", width=18,
                   command=self._update_c_list).grid(row=8, column=1, sticky=NW, padx=5, pady=10)
        ttk.Button(center_frame, text="Add Savings", width=14,
                   command=self._add_savings).grid(row=7, column=1, sticky=NW, padx=5, pady=0)
        ttk.Button(center_frame, text="Add Chequing", width=14,
                   command=self._add_chequings).grid(row=8, column=1, sticky=NW, padx=5, pady=10)
        ttk.Button(center_frame, text="Update Savings", width=16,
                   command=self._update_savings).grid(row=7, column=2, sticky=NW, padx=5, pady=0)
        ttk.Button(center_frame, text="Update Chequing", width=16,
                   command=self._update_chequings).grid(row=8, column=2, sticky=NW, padx=5, pady=10)
        ttk.Button(right_frame, text="Remove Account", width=21,
                   command=self._remove_account).grid(row=7, column=1, sticky=NW, padx=5, pady=0)
        ttk.Button(right_frame, text="Quit", width=21,
                   command=self._quit_callback).grid(row=8, column=1, sticky=NW, padx=5, pady=10)

        # Accounts ListBox
        tk.Label(left_frame, text="Account list", width=10, height=1).grid(row=1, column=1, columnspan=3, padx=5, pady=5)
        self._account_list = tk.Listbox(left_frame, width=16, height=8)
        self._account_list.grid(row=4, column=1, columnspan=10, padx=10, pady=22)
        # Call this on select
        self._account_list.bind("<<ListboxSelect>>", self._update_textbox)

        # Details Box
        tk.Label(center_frame, text="Details", width=10, height=1).grid(row=1, column=1, columnspan=2, padx=10, pady=5)
        self._info_text = tk.Text(master=center_frame, height=9, width=26, font=("TkTextFont", 10))
        self._info_text.grid(row=4, column=1, columnspan=10, padx=10, pady=22)
        self._info_text.tag_configure("bold", font=("TkTextFont", 10, "bold"))

        # Summary Box
        tk.Label(right_frame, text="Summary", width=10, height=1).grid(row=1, column=1, padx=10, pady=5)
        self._stat_list = tk.Listbox(right_frame, width=20, height=8)
        self._stat_list.grid(row=3, column=1, columnspan=10, padx=10, pady=22)

        # Now update the list
        self._update_account_list()
        self._update_stat_list()

    def _update_textbox(self, evt):
        """ Updates the info text box on the right, based on the current ID selected """

        # This is a list, so we take just the first item (could be multi select...)
        selected_values = self._account_list.curselection()
        selected_index = selected_values[0]
        account_id = self._account_list.get(selected_index)

        # Make a GET request
        r = requests.get("http://127.0.0.1:5000/bank/accounts/" + str(account_id))

        # Clear the text box
        self._info_text.delete(1.0, tk.END)

        # Check the request status code
        if r.status_code != 200:
            self._info_text.insert(tk.END, "Error running the request!")

        # For every item (key, value) in the JSON response, display them:
        for k, v in r.json().items():
            self._info_text.insert(tk.END, f"{k.capitalize()}\t\t", "bold")
            self._info_text.insert(tk.END, f"{v}\n")

    def _remove_account(self):
        """ Remove Account Popup """
        self._popup_win = tk.Toplevel()
        self._popup = RemoveAccountPopup(self._popup_win, self._close_account_cb)
        self._update_account_list()
        self._update_stat_list()

    def _close_account_cb(self):
        """ Close Remove Account Popup """
        self._popup_win.destroy()
        self._update_account_list()
        self._update_stat_list()

    def _add_savings(self):
        """ Add Savings Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddSavingsPopup(self._popup_win, self._close_savings_cb)
        self._update_account_list()
        self._update_stat_list()

    def _close_savings_cb(self):
        """ Close Add Savings Popup """
        self._popup_win.destroy()
        self._update_account_list()
        self._update_stat_list()

    def _add_chequings(self):
        """ Add Chequings Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddChequingsPopup(self._popup_win, self._close_chequings_cb)
        self._update_account_list()
        self._update_stat_list()

    def _close_chequings_cb(self):
        """ Close Add Chequings Popup """
        self._popup_win.destroy()
        self._update_account_list()
        self._update_stat_list()

    def _update_savings(self):
        """ Update Savings Popup """
        self._popup_win = tk.Toplevel()
        self._popup = UpdateSavingsPopup(self._popup_win, self._close_savings_update_cb)
        self._update_account_list()
        self._update_stat_list()

    def _close_savings_update_cb(self):
        """ Close Update Savings Popup """
        self._popup_win.destroy()
        self._update_account_list()
        self._update_stat_list()

    def _update_chequings(self):
        """ Update Chequings Popup """
        self._popup_win = tk.Toplevel()
        self._popup = UpdateChequingsPopup(self._popup_win, self._close_chequings_update_cb)
        self._update_account_list()
        self._update_stat_list()

    def _close_chequings_update_cb(self):
        """ Close Update Chequings Popup """
        self._popup_win.destroy()
        self._update_account_list()
        self._update_stat_list()

    def _quit_callback(self):
        """ Quit """
        self.quit()

    def _update_account_list(self):
        """ Update the List of Accounts """
        r = requests.get("http://127.0.0.1:5000/bank")
        self._account_list.delete(0, tk.END)
        for s in r.json():
            self._account_list.insert(tk.END, s['account_id'])

    def _update_s_list(self):
        """ Update the List of Savings Accounts """
        r = requests.get("http://127.0.0.1:5000/bank")
        self._account_list.delete(0, tk.END)
        for s in r.json():
            if s['type'] == "savings":
                self._account_list.insert(tk.END, s['account_id'])

    def _update_c_list(self):
        """ Update the List of Chequing Accounts """
        r = requests.get("http://127.0.0.1:5000/bank")
        self._account_list.delete(0, tk.END)
        for s in r.json():
            if s['type'] == "chequing":
                self._account_list.insert(tk.END, s['account_id'])

    def _update_stat_list(self):
        """ Update the summary"""
        r = requests.get("http://127.0.0.1:5000/bank")
        self._stat_list.delete(0, tk.END)
        num_savings = 0
        num_accounts = 0
        num_balance = 0
        num_transactions = 0
        num_sbalance = 0

        for s in r.json():
            num_accounts += 1
            num_balance += s["balance"]
            num_transactions += s["transactions"]
            if s["type"] == "savings":
                num_savings += 1
                num_sbalance += s["balance"]
        num_chequing = num_accounts - num_savings
        num_cbalance = num_balance - num_sbalance

        self._stat_list.insert(tk.END, f"Bank Accounts: {num_accounts}")
        self._stat_list.insert(tk.END, f"Savings Accounts: {num_savings}")
        self._stat_list.insert(tk.END, f"Chequing Accounts: {num_chequing}")
        self._stat_list.insert(tk.END, f"Bank Transactions: {num_transactions}")
        self._stat_list.insert(tk.END, f"Bank Total: ${num_balance}")
        self._stat_list.insert(tk.END, f"Savings Total: ${num_sbalance}")
        self._stat_list.insert(tk.END, f"Chequing Total: ${num_cbalance}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    MainAppController(root).pack()
    root.mainloop()