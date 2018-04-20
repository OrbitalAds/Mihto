from mihto.lexer.lexer import Token
import mihto.lexer.token_types as ttypes
from mihto.parser.nodes import ExpressionNode, VarRefNode, FloatNode, IntegerNode


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        expression = self._parse_expression()
        return expression

    def _parse_expression(self):
        if self.peek(ttypes.OPENPAR):
            self.consume(ttypes.OPENPAR)
            expression = self._parse_expression()
            self.consume(ttypes.CLOSEPAR)
        else:
            expression = self._parse_atomic_expression()
        return expression

    def _parse_atomic_expression(self) -> ExpressionNode:
        value1 = self._parse_value()
        operator = self._parse_operator()
        value2 = self._parse_value()
        expression = ExpressionNode(value1, operator, value2)
        if self.peek(ttypes.OPERATORS):
            operator2 = self._parse_operator()
            value3 = self._parse_value()
            expression = ExpressionNode(expression, ttypes.AND, ExpressionNode(expression.value2, operator2, value3))

        if self.peek(ttypes.LOGICAL_OPERATORS):
            logical_operator = self._parse_logical_operator()
            expression = ExpressionNode(expression, logical_operator, self._parse_expression())

        return expression

    def _parse_operator(self) -> str:
        if self.peek(ttypes.LESS_EQ_THAN):
            operator = self.consume(ttypes.LESS_EQ_THAN)
        elif self.peek(ttypes.LESS_THAN):
            operator = self.consume(ttypes.LESS_THAN)
        elif self.peek(ttypes.GREATER_EQ_THAN):
            operator = self.consume(ttypes.GREATER_EQ_THAN)
        elif self.peek(ttypes.GREATER_THAN):
            operator = self.consume(ttypes.GREATER_THAN)
        elif self.peek(ttypes.EQUALS):
            operator = self.consume(ttypes.EQUALS)
        else:
            operator = self.consume(ttypes.NOT_EQUALS)
        return operator.type

    def _parse_logical_operator(self) -> str:
        if self.peek(ttypes.AND):
            operator = self.consume(ttypes.AND)
        else:
            operator = self.consume(ttypes.OR)
        return operator.type

    def _parse_value(self):
        if self.peek(ttypes.FLOAT):
            node = self._parse_float()
        elif self.peek(ttypes.INTEGER):
            node = self._parse_integer()
        else:
            node = self._parse_varref()
        return node

    def _parse_varref(self) -> VarRefNode:
        return VarRefNode(self.consume(ttypes.IDENTIFIER).value)

    def _parse_float(self) -> FloatNode:
        return FloatNode(float(self.consume(ttypes.FLOAT).value))

    def _parse_integer(self) -> IntegerNode:
        return IntegerNode(int(self.consume(ttypes.INTEGER).value))

    def consume(self, expected_type: str) -> Token:
        token = self.tokens.pop(0)

        if token.type == expected_type:
            return token
        else:
            raise RuntimeError("Expected token type {} but got {} instead".format(expected_type, token.type))

    def peek(self, expected_type, offset=0) -> bool:
        if type(expected_type) is str:
            return self.tokens and self.tokens[offset].type == expected_type
        else:
            return self.tokens and self.tokens[offset].type in expected_type


