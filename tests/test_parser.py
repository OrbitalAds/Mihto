import unittest

from mihto import Parser, Lexer
import mihto.lexer.token_types as ttypes


class TestParser(unittest.TestCase):

    @staticmethod
    def parse(expression):
        tokens = Lexer(expression).tokenize()
        return Parser(tokens).parse()

    def test_parse_atomic_expression(self):
        expression = "123 = 123"
        parsed_expression = self.parse(expression)
        self.assertEqual("123 = 123", str(parsed_expression))

    def test_parse_wrapped_expression(self):
        expression = "(123 = 123)"
        parsed_expression = self.parse(expression)
        self.assertEqual("123 = 123", str(parsed_expression))

    def test_parse_atomic_chained_expression(self):
        expression = "1 < 2 < 3"
        parsed_expression = self.parse(expression)
        self.assertEqual("1 < 2 and 2 < 3", str(parsed_expression))

    def test_parse_or_expression(self):
        expression = "1 = 1 or 2 = 2"
        parsed_expression = self.parse(expression)
        self.assertEqual("1 = 1 or 2 = 2", str(parsed_expression))

    def test_parse_nested_expressions(self):
        expression = "(1 = 1) or ( (2 = 3) and (4 = 4))"
        parsed_expression = self.parse(expression)
        self.assertEqual(parsed_expression.operator, ttypes.OR)
        self.assertEqual(parsed_expression.value1.operator, ttypes.EQUALS)
        self.assertEqual(parsed_expression.value2.operator, ttypes.AND)
        self.assertEqual(parsed_expression.value2.value1.operator, ttypes.EQUALS)
        self.assertEqual(parsed_expression.value2.value2.operator, ttypes.EQUALS)
