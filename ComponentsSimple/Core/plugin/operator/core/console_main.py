import pkg_resources


def calc(operatori):
    try:
        first = input_number("Input the first number:")
        second = input_number("Input the second number:")
        # The user should choose the operator.
        operator = determine_operator(operatori)
        # Calls the "operation" method of a choosen operator
        result = operator.operation(first, second)
        print("Result is: {}".format(result))
    except Exception as e:
        print("Error: {}".format(e))


def input_number(poruka):
    success = False
    while not success:
        number, success = convert_to_int(input(poruka))
    return number


def determine_operator(operatori):
    while True:
        print("Choose an operator from the following list:")
        for i, o in enumerate(operatori):
            print(" {} {}  {}".format(i, o.operator_identifier(), o.operator_name()))
        choice = input_number("Type the option number:")
        if 0 <= choice < len(operatori):
            return operatori[choice]


def convert_to_int(number_str, default=0):
    """
    This function tries to conver a string to an integer.
    :param number_str: string representation of a int
    :param default: default value to return if the conversion fails
    :return: If the conversion succeeded, the first return value
             is converted integer, while the second value is True.
             Otherwise, the (default, False) is returned.
    """
    try:
        value = int(number_str)
        return value, True
    except:
        value = default
        return value, False


def load_plugins():
    """
    This functions dynamically determines available plugins
    that belong to the group 'core.operator'
    """
    operators = []
    for ep in pkg_resources.iter_entry_points(group='core.operator'):
        o = ep.load()
        # Show the name of an entry point and the object exported
        # as an entry point.
        # In this case, entry point is the operator class.
        print("{} {}".format(ep.name, o))
        # instantiate an operator
        operator = o()
        operators.append(operator)
    return operators


def main():
    """
    Whe running "operator_main" command in the terminal session (console),
    this function executes.
    It dynamically load plugins and the ask user for the input.
    """
    try:
        operators = load_plugins()
        if len(operators) == 0:
            print("No available plugins.")
            return
    except Exception as e:
        print("Error: {}".format(e))
        return

    while True:
        print("---------------------------------------------")
        calc(operators)
        choice = input("Press enter to proceed or press q to exit the application.")
        if choice == "q":
            break


if __name__ == "__main__":
    main()
