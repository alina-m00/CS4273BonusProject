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
