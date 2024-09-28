from enum import Enum

class Operation(Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"

    @classmethod
    def strings(this) -> str:
        return ", ".join(operation.value for operation in this)


def perform_operation(num1: float, num2 : float, opearation : str) -> float:
    match opearation:
        case Operation.ADD.value:
            return num1 + num2
        case Operation.SUBTRACT.value:
            return num1 - num2
        case Operation.MULTIPLY.value:
            return num1 * num2
        case Operation.DIVIDE.value:
            if num2 == 0:
                print("Division by zero is not allowed")
            return num1 / num2
        case _:
            print("Invalid operation. Please select one from : " + Operation.strings())
