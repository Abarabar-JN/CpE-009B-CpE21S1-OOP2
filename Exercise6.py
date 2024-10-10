from tkinter import *


class MyWindow:
    def __init__(self, win):
        win.configure(bg="#000000")
        self.Lbl1 = Label(win, fg="Gold", text=" Simple Calculator ࣪", bg="#008000", font=("Comic Sans MS", 24))
        self.Lbl1.place(x=70, y=20)
        self.Lbl2 = Label(win, text="1st Number:", bg="#FFA500", font=("Trebuchet MS", 10))
        self.Lbl2.place(x=50, y=80)
        self.t1 = Entry(win, bd=2, width=15)
        self.t1.place(x=150, y=80)
        self.Lbl3 = Label(win, text="2nd Number:", bg="#FFA500", font=("Trebuchet MS", 10))
        self.Lbl3.place(x=50, y=130)
        self.t2 = Entry(win, bd=2, width=15)
        self.t2.place(x=150, y=130)
        self.Lbl4 = Label(win, text="Result:", bg="#FFA500", font=("Trebuchet MS", 10))
        self.Lbl4.place(x=50, y=180)
        self.t3 = Entry(win, bd=2, width=15, state='readonly')
        self.t3.place(x=150, y=180)
        button_frame = Frame(win, bg="#FFA500")
        button_frame.place(x=90, y=220)
        self.Btn1 = Button(button_frame, bg="lightcoral", fg="Red", text="Add", font=("Lucida Console", 10),
                           command=self.add)
        self.Btn1.grid(row=0, column=0, padx=5)
        self.Btn2 = Button(button_frame, bg="lightblue", fg="Blue", text="Subtract", font=("Lucida Console", 10),
                           command=self.subtract)
        self.Btn2.grid(row=0, column=1, padx=5)
        self.Btn3 = Button(button_frame, bg="lightgreen", fg="Green", text="Multiply", font=("Lucida Console", 10),
                           command=self.multiply)
        self.Btn3.grid(row=0, column=2, padx=5)
        self.Btn4 = Button(button_frame, bg="lightpink", fg="Purple", text="Divide", font=("Lucida Console", 10),
                           command=self.divide)
        self.Btn4.grid(row=0, column=3, padx=5)

        self.Btn5 = Button(win, bg="deepskyblue", fg="Blue", text="Clear", font=("Lucida Console", 10),
                           command=self.clear)
        self.Btn5.place(x=150, y=260)

    def add(self):
        self.t3.config(state='normal')
        num1 = self.get_number(self.t1)
        num2 = self.get_number(self.t2)
        self.t3.delete(0, 'end')
        self.t3.insert(END, str(num1 + num2))
        self.t3.config(state='readonly')

    def subtract(self):
        self.t3.config(state='normal')
        num1 = self.get_number(self.t1)
        num2 = self.get_number(self.t2)
        self.t3.delete(0, 'end')
        self.t3.insert(END, str(num1 - num2))
        self.t3.config(state='readonly')

    def multiply(self):
        self.t3.config(state='normal')
        num1 = self.get_number(self.t1)
        num2 = self.get_number(self.t2)
        self.t3.delete(0, 'end')
        self.t3.insert(END, str(num1 * num2))
        self.t3.config(state='readonly')

    def divide(self):
        self.t3.config(state='normal')
        num1 = self.get_number(self.t1)
        num2 = self.get_number(self.t2)
        self.t3.delete(0, 'end')
        if num2 != 0:
            self.t3.insert(END, str(num1 / num2))
        else:
            self.t3.insert(END, "Error")
        self.t3.config(state='readonly')

    def clear(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.config(state='normal')
        self.t3.delete(0, 'end')
        self.t3.config(state='readonly')

    def get_number(self, entry):
        try:
            return float(entry.get())
        except ValueError:
            return 0.0


# Main window
window = Tk()
mywin = MyWindow(window)
window.geometry("400x320+10+10")
window.title("Simple Calculator")
window.mainloop()
