import tkinter as tk
from registration import RegistrationForm

def main():
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()

