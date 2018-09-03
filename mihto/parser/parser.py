from typing import Union

from mihto.lexer.lexer import Token
import mihto.lexer.token_types as ttypes
from mihto.parser.exceptions import UnexpectedTokenFoundException
from mihto.parser.nodes import ExpressionNode, VarRefNode, FloatNode, IntegerNode, ValueNode


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self) -> Union[ExpressionNode, None]:
        if not self.tokens:
            return None
        expression = self._parse_expression()
        return expression

    def _parse_expression(self) -> ExpressionNode:
        expression = self._parse_expression0()
        if self.peek(ttypes.COMP_OPERATORS):
            operator = self._parse_comp_operator()
            right_expression = self._parse_expression()
            expression = ExpressionNode(expression, operator, right_expression)
        return expression

    def _parse_expression0(self) -> ExpressionNode:
        expression = self._parse_expression1()
        if self.peek([ttypes.OR, ttypes.PLUS, ttypes.SCORE]):
            operator = self._parse_operator_0()
            right_expression = self._parse_expression0()
            expression = ExpressionNode(expression, operator, right_expression)
        return expression

    def _parse_expression1(self):
        expression = self._parse_atomic_expression()
        if self.peek([ttypes.AND, ttypes.ASTERISK, ttypes.BACKSLASH]):
            operator = self._parse_operator_1()
            right_expression = self._parse_expression1()
            expression = ExpressionNode(expression, operator, right_expression)
        return expression

    def _parse_atomic_expression(self) -> ExpressionNode:
        if self.peek([ttypes.INTEGER, ttypes.FLOAT, ttypes.IDENTIFIER]):
            expression = self._parse_value()
        else:
            self.consume(ttypes.OPENPAR)
            expression = self._parse_expression()
            self.consume(ttypes.CLOSEPAR)

        return expression

    def _parse_comp_operator(self) -> str:
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

    def _parse_operator_0(self) -> str:
        return self.consume([ttypes.OR, ttypes.PLUS, ttypes.SCORE]).type

    def _parse_operator_1(self) -> str:
        return self.consume([ttypes.AND, ttypes.ASTERISK, ttypes.BACKSLASH]).type

    def _parse_value(self) -> ValueNode:
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

    def _check_type(self, expected_type: Union[str, list], token) -> bool:
        expected_type = [expected_type] if type(expected_type) is str else expected_type
        return token.type in expected_type

    def consume(self, expected_type: Union[str, list]) -> Token:
        token = self.tokens.pop(0)
        if self._check_type(expected_type, token):
            return token
        else:
            raise UnexpectedTokenFoundException(
                "Expected token type {} but got {} instead".format(expected_type, token.type))

    def peek(self, expected_type : Union[str, list], offset=0) -> bool:
            return self.tokens and self._check_type(expected_type, self.tokens[offset])
