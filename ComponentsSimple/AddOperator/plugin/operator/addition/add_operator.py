from plugin.operator.core.services.operator import OperatorBase


class AddOperator(OperatorBase):
    """
    Concrete implementation of addition operator.

    The OperatorBase abstract class is provided by the Code component.
    """

    def operator_name(self):
        return "Addition"

    def operator_identifier(self):
        return "AdditionOperator"

    def operation(self, number1, number2):
        return number1 + number2
