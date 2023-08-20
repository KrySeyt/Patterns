"""
Grammar:

BooleanExpression ::= VariableExpression | Constant | OrExpression | AndExpression | NotExpression |
"(" BooleanExpression ")"
AndExpression ::= BooleanExpression "and" BooleanExpression
OrExpression ::= BooleanExpression "or" BooleanExpression
NotExpression ::= "not" BooleanExpression
Constant ::= "True" | "False"
VariableExpression ::= "A" | "B" | ... | "X" | "Y" | "Z"
"""

from abc import ABC, abstractmethod


class Context:
    def __init__(self) -> None:
        self._context: dict[str, bool] = {}

    def add(self, variable_name: str, value: bool) -> None:
        self._context[variable_name] = value

    def get(self, variable_name: str) -> bool | None:
        return self._context.get(variable_name, None)


class BooleanExpression(ABC):
    @abstractmethod
    def evaluate(self, context: Context) -> bool | None:
        raise NotImplementedError

    def replace(self, variable_name: str, expression: "BooleanExpression") -> "BooleanExpression":
        raise NotImplementedError


# Terminal expression
class VariableExpression(BooleanExpression):
    def __init__(self, variable_name: str) -> None:
        self.variable_name = variable_name

    def evaluate(self, context: Context) -> bool | None:
        return context.get(self.variable_name)

    def replace(self, variable_name: str, expression: "BooleanExpression") -> "BooleanExpression":
        if variable_name == self.variable_name:
            return expression
        return VariableExpression(self.variable_name)


# Non-terminal expression
class AndExpression(BooleanExpression):
    def __init__(self, first_operand: BooleanExpression, second_operand: BooleanExpression) -> None:
        self.first_operand = first_operand
        self.second_operand = second_operand

    def evaluate(self, context: Context) -> bool | None:
        return (self.first_operand.evaluate(context) and
                self.second_operand.evaluate(context))

    def replace(self, variable_name: str, expression: "BooleanExpression") -> "AndExpression":
        return AndExpression(
            self.first_operand.replace(variable_name, expression),
            self.second_operand.replace(variable_name, expression)
        )


class OrExpression(BooleanExpression):
    def __init__(self, first_operand: BooleanExpression, second_operand: BooleanExpression) -> None:
        self.first_operand = first_operand
        self.second_operand = second_operand

    def evaluate(self, context: Context) -> bool | None:
        return (self.first_operand.evaluate(context) or
                self.second_operand.evaluate(context))

    def replace(self, variable_name: str, expression: "BooleanExpression") -> "OrExpression":
        return OrExpression(
            self.first_operand.replace(variable_name, expression),
            self.second_operand.replace(variable_name, expression)
        )


class NotExpression(BooleanExpression):
    def __init__(self, operand: BooleanExpression) -> None:
        self.operand = operand

    def evaluate(self, context: Context) -> bool | None:
        return not self.operand.evaluate(context)

    def replace(self, variable_name: str, expression: "BooleanExpression") -> "NotExpression":
        return NotExpression(self.operand.replace(variable_name, expression))


class Constant(BooleanExpression):
    def __init__(self, value: bool) -> None:
        self.value = value

    def evaluate(self, context: Context) -> bool | None:
        return self.value

    def replace(self, variable_name: str, expression: "BooleanExpression") -> "BooleanExpression":
        return expression


def main() -> None:
    # X or Y

    context = Context()
    context.add("X", True)
    context.add("Y", False)

    x = VariableExpression("X")
    y = VariableExpression("Y")

    or_expression = OrExpression(x, y)
    print(or_expression.evaluate(context))

    # (True and X) and (Y or False)

    context.add("X", False)
    context.add("Y", True)

    and_expression = AndExpression(
        AndExpression(Constant(True), x),
        OrExpression(y, Constant(False))
    )
    print(and_expression.evaluate(context))


if __name__ == "__main__":
    main()




