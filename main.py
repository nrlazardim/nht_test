from getting import CalculatorMenu, operator_number, first_number, second_number
from creating import Add, Subtract, Multiply, Division


def run():
    is_created = True

    while is_created:

        menu_calculator = CalculatorMenu(ADD="1: Add", SUBTRACT="2: Subtract", MULTIPLY="3: Multiply",
                                         DIVIDE="4: Divide", EXIT="5: Exit")
        print(f"{menu_calculator}")
        operator = operator_number()

        if operator in (1, 2, 3, 4, 5):  # Make sure the user have entered the valid choice
            if operator == 5:  # first check whether user want to exit
                print("\n Thank you for choosing us \n ----------- Exit program ------------")
                break

            # If not then ask fo the input and call appropiate methods
            value_1 = first_number()
            value_2 = second_number()

            if operator == 1:
                add_option = Add(value_1=value_1, value_2=value_2)
                print(f"{value_1} + {value_2} = {add_option.operator_add}")

            elif operator == 2:
                subtract_option = Subtract(value_1=value_1, value_2=value_2)
                print(f"{value_1} - {value_2} = {subtract_option.operator_subtract}")

            elif operator == 3:
                multiply_option = Multiply(value_1=value_1, value_2=value_2)
                print(f"{value_1} * {value_2} = {multiply_option.operator_multiply}")

            elif operator == 4:
                division_option = Division(value_1=value_1, value_2=value_2)
                print(f"{value_1} / {value_2} = {division_option.operator_division}")


if __name__ == "__main__":  # execute only if the file was run directly, and not imported.
    run()
