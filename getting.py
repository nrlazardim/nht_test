from dataclasses import dataclass


@dataclass()
class CalculatorMenu:
    ADD: str
    SUBTRACT: str
    MULTIPLY: str
    DIVIDE: str
    EXIT: str

    def __repr__(self):
        phrase_to_show = f'''This is a {self.__class__.__name__} select a option \n {self.ADD} \n {self.SUBTRACT} \n {self.MULTIPLY} \n {self.DIVIDE} \n {self.EXIT}.'''
        return phrase_to_show


def operator_number():
    try:
        number = float(input("Select operation: "))
        return number
    except ValueError:
        print("Use a int or float number")


def first_number():
    try:
        number = float(input("Enter first number: "))
        return number
    except ValueError:
        print("Use a int or float number")


def second_number():
    try:
        number = float(input("Enter first number: "))
        return number
    except ValueError:
        print("Use a int or float number")


