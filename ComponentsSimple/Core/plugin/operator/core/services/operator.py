from abc import ABC, abstractmethod


class OperatorBase(ABC):
    """
    An abstract implementation of a math operator.

    This class is expected to be overridden by a class that represents
    the concrete implementation of math operator provided in plugin.
    """

    @abstractmethod
    def operator_identifier(self):
        """
        A unique identifier of concrete operator.
        """
        pass

    @abstractmethod
    def operator_name(self):
        """
        A name operator.
        """
        pass

    @abstractmethod
    def operation(self, number1, number2):
        """
        Implementation of the corresponding math operation.
        """
        pass
