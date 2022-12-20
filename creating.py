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
            print("XXXXXXXXXXXXXXX")  # TODO
        except TypeError:
            print("XXXXXXXXXXXXXXXXXXX")
        except ValueError:
            print("XXXXXXXXXXXXXXXXXXX")



    @staticmethod
    def subtract(value_1: float, value_2: float) -> float:
        try:
            subtracting_value = operator.sub(value_1, value_2)
            return subtracting_value
        except OverflowError:
            print("Math out of range as overflow error")
        except FloatingPointError:
            print("XXXXXXXXXXXXXXX")  # TODO
        except TypeError:
            print("XXXXXXXXXXXXXXXXXXX")
        except ValueError:
            print("XXXXXXXXXXXXXXXXXXX")

    @staticmethod
    def multiply(value_1: float, value_2: float) -> float:
        try:
            multiplying_value = operator.mul(value_1, value_2)
            return multiplying_value
        except OverflowError:
            print("Math out of range as overflow error")
        except FloatingPointError:
            print("XXXXXXXXXXXXXXX")  # TODO
        except TypeError:
            print("XXXXXXXXXXXXXXXXXXX")
        except ValueError:
            print("XXXXXXXXXXXXXXXXXXX")

    @staticmethod
    def division(value_1: float, value_2: float) -> float:  # ZeroDivisionError
        try:
            division_value = operator.truediv(value_1, value_2)
            return division_value
        except ZeroDivisionError:
            print(f"Division by zero not allowed try again")
        except OverflowError:
            print("Math out of range as overflow error")
        except FloatingPointError:
            print("XXXXXXXXXXXXXXX")  # TODO
        except TypeError:
            print("XXXXXXXXXXXXXXXXXXX")  # TODO
        except ValueError:
            print("XXXXXXXXXXXXXXXXXXX")
