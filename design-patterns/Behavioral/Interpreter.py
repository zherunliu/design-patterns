from abc import ABC, abstractmethod
from typing import List
from sys import stdin


# abstract expression
class Expression(ABC):
    @abstractmethod
    def interpret(self) -> int:
        pass


# terminal expression
class NumberExpression(Expression):
    def __init__(self, value: int) -> None:
        self.value = value

    def interpret(self) -> int:
        return self.value


# non-terminal expressions
class AddExpression(Expression):
    def __init__(self, left: NumberExpression, right: NumberExpression) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() + self.right.interpret()


class MultiplyExpression(Expression):
    def __init__(self, left: NumberExpression, right: NumberExpression) -> None:
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() * self.right.interpret()


def parse_expression(expression: str):
    elements = expression.split()
    stack_num: List[NumberExpression] = []
    stack_opera: List[str] = []

    for ele in elements:
        if ele.isdigit():
            stack_num.append(NumberExpression(int(ele)))
        elif ele == "+":
            while stack_opera and stack_opera[-1] == "*":
                right = stack_num.pop()
                left = stack_num.pop()
                stack_num.append(
                    NumberExpression(MultiplyExpression(left, right).interpret())
                )
                stack_opera.pop()
            stack_opera.append("+")
        elif ele == "*":
            stack_opera.append("*")
        else:
            raise ValueError("Invalid expression format")

    while stack_opera:
        opera = stack_opera.pop()
        if opera == "+":
            right = stack_num.pop()
            left = stack_num.pop()
            stack_num.append(NumberExpression(AddExpression(left, right).interpret()))
        elif opera == "*":
            right = stack_num.pop()
            left = stack_num.pop()
            stack_num.append(
                NumberExpression(MultiplyExpression(left, right).interpret())
            )
        else:
            raise ValueError("Invalid expression format")

    return stack_num.pop().interpret()


if __name__ == "__main__":
    input_lines: List[str] = []
    for line in stdin:
        input_lines.append(line.strip())

    for input_line in input_lines:
        try:
            result = parse_expression(input_line)
            print(result)
        except ValueError as e:
            print(e)
