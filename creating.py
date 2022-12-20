import operator


class Calculator:

    @staticmethod
    def add(value_1: float, value_2: float) -> float:
        try:
            adding_value = operator.add(value_1, value_2)
            return adding_value
        except OverflowError:
            print("Math out of range as overflow error")
        except FloatingPointError:
            print("Decimal fractions cannot be represented exactly as binary (base 2) fractions.")
        except TypeError:
            print("Please enter a number")
        except ValueError:
            print("Value of an inappropriate type")

    @staticmethod
    def subtract(value_1: float, value_2: float) -> float:
        try:
            subtracting_value = operator.sub(value_1, value_2)
            return subtracting_value
        except OverflowError:
            print("Math out of range as overflow error")
        except FloatingPointError:
            print("Decimal fractions cannot be represented exactly as binary (base 2) fractions.")
        except TypeError:
            print("Please enter a number")
        except ValueError:
            print("Value of an inappropriate type")

    @staticmethod
    def multiply(value_1: float, value_2: float) -> float:
        try:
            multiplying_value = operator.mul(value_1, value_2)
            return multiplying_value
        except OverflowError:
            print("Math out of range as overflow error")
        except FloatingPointError:
            print("Decimal fractions cannot be represented exactly as binary (base 2) fractions.")
        except TypeError:
            print("Please enter a number")
        except ValueError:
            print("Value of an inappropriate type")

    @staticmethod
    def division(value_1: float, value_2: float) -> float:  # ZeroDivisionError
        try:
            division_value = operator.truediv(value_1, value_2)
            return division_value
        except ZeroDivisionError:
            print(f"Division by zero not allowed")
        except OverflowError:
            print("Math out of range as overflow error")
        except FloatingPointError:
            print("Decimal fractions cannot be represented exactly as binary (base 2) fractions.")
        except TypeError:
            print("Please enter a number")
        except ValueError:
            print("Value of an inappropriate type")
