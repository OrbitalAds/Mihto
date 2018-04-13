from mihto.parser.nodes import ExpressionNode
import mihto.lexer.token_types as ttypes

class Evaluator:
    OPS = {
        ttypes.AND: lambda x, y: x and y,
        ttypes.OR: lambda x, y: x or y,
        ttypes.LESS_EQ_THAN: lambda x, y: x <= y,
        ttypes.LESS_THAN: lambda x, y: x < y,
        ttypes.GREATER_EQ_THAN: lambda x, y: x >= y,
        ttypes.GREATER_THAN: lambda x, y: x > y,
        ttypes.EQUALS: lambda x, y: x == y,
        ttypes.NOT_EQUALS: lambda x, y: x != y
    }

    def __init__(self, env: dict):
        self.env = env

    def evaluate(self, expression: ExpressionNode) -> bool:
        operator = expression.operator

        if operator in ttypes.LOGICAL_OPERATORS:
            return Evaluator.OPS[operator](self.evaluate(expression.value1), self.evaluate(expression.value2))

        if type(expression.value1) is ExpressionNode or type(expression.value2) is ExpressionNode:
            raise RuntimeError("Operator mismatch. Cannot perform {} operator with boolean data".format(operator))

        value1, value2 = expression.value1.value, expression.value2.value

        if type(value1) is str:
            value1 = self.env.get(value1, None)
            if value1 is None:
                raise RuntimeError("{} cannot be found in environment".format(value1))
        if type(value2) is str:
            value2 = self.env.get(value2, None)
            if value2 is None:
                raise RuntimeError("{} cannot be found in environment".format(value2))

        return Evaluator.OPS[operator](value1, value2)