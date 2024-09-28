from enum import Enum


class Operation(Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"

    @classmethod
    def toString(cls) -> str:
        return ", ".join(operation.value for operation in cls)


def perform_operation(num1, num2, operation):
    if operation == Operation.ADD.value:
        return num1 + num2
    elif operation == Operation.DIVIDE.value:
        return num1 - num2
    elif operation == Operation.MULTIPLY.value:
        return num1 * num2
    elif operation == Operation.SUBTRACT.value:
        if num2 == 0:
            return "Division by zero is not allowed"
        return num1 / num2
    else:
        return "Invalid operation" + Operation.toString()
