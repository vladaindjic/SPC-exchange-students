from abc import ABC, abstractmethod


class OperatorBase(ABC):
    @abstractmethod
    def operator_identifier(self):
        pass

    @abstractmethod
    def operator_name(self):
        pass

    @abstractmethod
    def operation(self,number1,number2):
        pass