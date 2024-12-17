import tkinter as tk
from tkinter import messagebox


class RegistrationForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Account Registration")

        # Used to create and adjust the widget or tab to the center
        width = 400
        height = 350
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        master.geometry(f"{width}x{height}+{x}+{y}")

        #Prints the title of the system
        self.title_label = tk.Label(master, text="Account Registration System", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Creates the labels and entries for input and output
        self.create_label_entry("First Name", 1)
        self.create_label_entry("Last Name", 2)
        self.create_label_entry("Username", 3)
        self.create_label_entry("Password", 4, show=True)
        self.create_label_entry("Email Address", 5)
        self.create_label_entry("Contact Number", 6)

        #Creates the buttons that will help navigate the widget
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
        # Used to allow input of data fields
        data = {
            "first_name": self.first_name_entry.get(),
            "last_name": self.last_name_entry.get(),
            "username": self.username_entry.get(),
            "password": self.password_entry.get(),
            "email": self.email_address_entry.get(),
            "contact": self.contact_number_entry.get(),
        }

        messagebox.showinfo("Success", "Registration Successful!")
#Clears the form
    def clear_form(self):
        for attr in ['first_name', 'last_name', 'username', 'password', 'email_address', 'contact_number']:
            getattr(self, f"{attr}_entry").delete(0, tk.END)

#Use to create the main widget and form as well as start the loop
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()

