import tkinter
from tkinter import *
from tkinter import messagebox

class Calculator:
    def __init__(self, gui):
        self.expression = ""
        self.operand = 0
        self.operator = ""
        
        self.display = StringVar()
        
        self.create_gui(gui)

    def append_digit(self, digit):
        self.expression += str(digit)
        self.display.set(self.expression)

    def handle_operator(self, op):
        self.operand = float(self.expression)
        self.operator = op
        self.expression += op
        self.display.set(self.expression)

    def clear_input(self):
        self.expression = ""
        self.operand = 0
        self.operator = ""
        self.display.set(self.expression)

    def calculate_result(self):
        input_expression = self.expression
        if self.operator in ["+", "-", "*", "/"]:
            second_operand = float((input_expression.split(self.operator)[1]))
            if self.operator == "+":
                result = self.operand + second_operand
            elif self.operator == "-":
                result = self.operand - second_operand
            elif self.operator == "*":
                result = self.operand * second_operand
            elif self.operator == "/":
                if second_operand == 0:
                    messagebox.showerror("Division by 0 Not Allowed.")
                    self.clear_input()
                    return
                else:
                    result = float(self.operand / second_operand)

            result_str = str(result)
            if '.' in result_str:
                integer_part, decimal_part = result_str.split('.')
                if len(integer_part) + len(decimal_part) > 9:
                    self.display.set("ERR")
                    return
            elif len(result_str) > 9:
                self.display.set("ERR")
                return

            self.display.set(result_str)
            self.expression = result_str

    def create_gui(self, gui):
        gui.geometry("320x500+400+400")
        gui.resizable(0, 0)
        gui.title("Unique Bonus Calculator")

        display_label = Label(
            gui,
            text="Expression",
            anchor=SE,
            font=("Calibri Math", 20),
            textvariable=self.display,
            background="#ffffff",
            fg="#000000"
        )
        display_label.pack(expand=True, fill="both")

        button_layout = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["AC", "C"]
        ]

        for row in button_layout:
            self.create_button_frame(gui, row)

    def create_button_frame(self, gui, buttons):
        frame = Frame(gui, bg="#000000")
        frame.pack(expand=True, fill="both")

        for text in buttons:
            if text == "AC":
                button = Button(
                    frame,
                    text=text,
                    font=("Calibri", 22),
                    relief=GROOVE,
                    border=0,
                    command=self.clear_input
                )
            else:
                button = Button(
                    frame,
                    text=text,
                    font=("Calibri", 22),
                    relief=GROOVE,
                    border=0,
                    command=lambda t=text: self.on_button_click(t)
                )
            button.pack(side=LEFT, expand=True, fill="both")

    def on_button_click(self, button_text):
        if button_text.isdigit() or button_text == ".":
            self.append_digit(button_text)
        elif button_text in ["+", "-", "*", "/"]:
            self.handle_operator(button_text)
        elif button_text == "=":
            self.calculate_result()
        elif button_text == "C":
            self.clear_input()

if __name__ == "__main__":
    guiWindow = tkinter.Tk()
    calculator = Calculator(guiWindow)
    guiWindow.mainloop()
