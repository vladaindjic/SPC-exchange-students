from plugin.operator.core.services.operator import OperatorBase


class SubtractOperator(OperatorBase):
    """
    The concrete implementation of subtraction operator.

    The OperatorBase class is provided by the Core component.
    """

    def operator_name(self):
        return "Subtraction"

    def operator_identifier(self):
        return "SubtractionOperation"

    def operation(self, number1, number2):
        return number1 - number2
