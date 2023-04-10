symbols = ["+", "-", "*", "/"]

class Calculator:
    def __init__(self, first_digit, second_digit, operation):
        self.first_digit = first_digit
        self.second_digit = second_digit
        self.operation = operation

    def __repr__(self):
        return "This is a string for the calculator"
    
    @classmethod
    def get_first_digit(cls):
        while True:
            try:
                return int(input("Please enter the first number: "))
            except ValueError:
                print("Invalid entry. Please enter a valid first number. ")

    @classmethod
    def get_second_digit(cls):
        while True:
            try:
                return int(input("Please enter the second number: "))
            except ValueError:
                print("Invalid entry. Please enter a valid second number. ")

    @classmethod
    def get_operation(cls):
        operation = input("Please indicate which operation you would like to use (+, -, *, /): ")
        while operation not in symbols:
            operation = input("That is not a valid input. Please enter one of the following (+, -, *, /)")
        return operation
               
    
    def get_formulate(self):
        if self.operation == "+":
            return self.first_digit + self.second_digit
        if self.operation == "-":
            return self.first_digit - self.second_digit
        if self.operation == "*":
            return self.first_digit * self.second_digit
        if self.operation == "/":
            return round(self.first_digit / self.second_digit, 2)


first_digit = Calculator.get_first_digit()
second_digit = Calculator.get_second_digit()
operation = Calculator.get_operation()
calculate = Calculator(first_digit, second_digit, operation)
print(calculate.get_formulate())