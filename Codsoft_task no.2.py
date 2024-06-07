import tkinter as tk
from math import sqrt

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x400")
        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self, button=None):
        input_frame = tk.Frame(self.root, bd=0, relief=tk.RAISED)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=2, width=28, borderwidth=4)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        buttons_frame = tk.Frame(self.root, bg="grey")
        buttons_frame.pack()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+', '=',
            'C', '%', '^', '√'
        ]

        row = 0
        col = 0
        for button in buttons:
            button_style = tk.Button(buttons_frame, text=button, font=('arial', 18, 'bold'), fg="black", width=4, height=1, bd=1, bg="#fff", command=lambda button=button: self.button_click(button))
            button_style.grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, button):
        if button == "C":
            self.expression = ""
            self.input_text.set(self.expression)
        elif button == "=":
            self.calculate_result()
        elif button == '√':
            try:
                self.expression = str(sqrt(float(self.expression)))
                self.input_text.set(self.expression)
            except:
                self.input_text.set("Error")
                self.expression = ""
        elif button == '^':
            self.expression += '**'
            self.input_text.set(self.expression)
        elif button == '%':
            try:
                self.expression = str(eval(self.expression) / 100)
                self.input_text.set(self.expression)
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += button
            self.input_text.set(self.expression)

    def calculate_result(self):
        try:
            self.expression = str(eval(self.expression))
            self.input_text.set(self.expression)
        except:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
