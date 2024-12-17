import tkinter as tk
from tkinter import messagebox
import csv
import os


class RegistrationForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Account Registration")

        width = 400
        height = 350
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        master.geometry(f"{width}x{height}+{x}+{y}")

        self.title_label = tk.Label(master, text="Account Registration System", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        self.create_label_entry("First Name", 1)
        self.create_label_entry("Last Name", 2)
        self.create_label_entry("Username", 3)
        self.create_label_entry("Password", 4, show=True)
        self.create_label_entry("Email Address", 5)
        self.create_label_entry("Contact Number", 6)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=7, column=0, pady=(20, 10), padx=(50, 5), sticky='e')

        self.clear_button = tk.Button(master, text="Clear", command=self.clear_form)
        self.clear_button.grid(row=7, column=1, pady=(20, 10), padx=(5, 50), sticky='w')

    def create_label_entry(self, label_text, row, show=False):
        label = tk.Label(self.master, text=label_text)
        label.grid(row=row, column=0, padx=(10, 5), sticky='e')

        entry = tk.Entry(self.master, show='*' if show else '')
        entry.grid(row=row, column=1, padx=(5, 10), sticky='w')
        setattr(self, f"{label_text.lower().replace(' ', '_')}_entry", entry)

    def submit_form(self):
        data = {
            "first_name": self.first_name_entry.get(),
            "last_name": self.last_name_entry.get(),
            "username": self.username_entry.get(),
            "password": self.password_entry.get(),
            "email": self.email_address_entry.get(),
            "contact": self.contact_number_entry.get(),
        }

        for field, value in data.items():
            if not value:
                messagebox.showerror("Missing Information",
                                     f"Please fill in the {field.replace('_', ' ').capitalize()} field.")
                return

        self.save_to_csv(data)

        messagebox.showinfo("Success", "Registration Successful!")

        self.clear_form()

    def save_to_csv(self, data):
        file_exists = os.path.isfile('registrations.csv')

        with open('registrations.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file,
                                    fieldnames=["first_name", "last_name", "username", "password", "email", "contact"])

            if not file_exists:
                writer.writeheader()

            writer.writerow(data)

    def clear_form(self):
        for attr in ['first_name', 'last_name', 'username', 'password', 'email_address', 'contact_number']:
            getattr(self, f"{attr}_entry").delete(0, tk.END)


def main():
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()


if __name__ == "__main__":
    main()
