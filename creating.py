from dataclasses import dataclass
import operator


@dataclass()
class Add:
    value_1: float
    value_2: float

    @classmethod
    def operator(cls, value_1: float, value_2: float):
        instance = cls(value_1=value_1, value_2=value_2)
        return instance

    @property
    def operator_add(self) -> float:
        try:
            return operator.add(self.value_1, self.value_2)
        except OverflowError:
            print("Math out of range as overflow error")
        except FloatingPointError:
            print("Decimal fractions cannot be represented exactly as binary (base 2) fractions.")
        except TypeError:
            print("Please enter a number")
        except ValueError:
            print("Value of an inappropriate type")


@dataclass()
class Subtract:
    value_1: float
    value_2: float

    @classmethod
    def operator(cls, value_1: float, value_2: float):
        instance = cls(value_1=value_1, value_2=value_2)
        return instance

    @property
    def operator_subtract(self) -> float:
        try:
            return operator.sub(self.value_1, self.value_2)
        except OverflowError:
            print("Math out of range as overflow error")
        except FloatingPointError:
            print("Decimal fractions cannot be represented exactly as binary (base 2) fractions.")
        except TypeError:
            print("Please enter a number")
        except ValueError:
            print("Value of an inappropriate type")


@dataclass()
class Multiply:
    value_1: float
    value_2: float

    @classmethod
    def operator(cls, value_1: float, value_2: float):
        instance = cls(value_1=value_1, value_2=value_2)
        return instance

    @property
    def operator_multiply(self) -> float:
        try:
            return operator.mul(self.value_1, self.value_2)
        except OverflowError:
            print("Math out of range as overflow error")
        except FloatingPointError:
            print("Decimal fractions cannot be represented exactly as binary (base 2) fractions.")
        except TypeError:
            print("Please enter a number")
        except ValueError:
            print("Value of an inappropriate type")


@dataclass()
class Division:
    value_1: float
    value_2: float

    @classmethod
    def operator(cls, value_1: float, value_2: float):
        instance = cls(value_1=value_1, value_2=value_2)
        return instance

    @property
    def operator_division(self) -> float:
        try:
            division_value = operator.truediv(self.value_1, self.value_2)
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
