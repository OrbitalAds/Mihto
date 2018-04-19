import unittest

from mihto import Lexer
import mihto.lexer.token_types as ttypes


class TestLexer(unittest.TestCase):


    def test_tokenize_integer(self):
        expression = "1"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.INTEGER)

    def test_tokenize_float(self):
        expression = "1.23"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.FLOAT)

    def test_tokenize_identifier_char_lower(self):
        expression = "a"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.IDENTIFIER)

    def test_tokenize_identifier_char_upper(self):
        expression = "a"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.IDENTIFIER)

    def test_tokenize_identifier_phrase_lower(self):
        expression = "abc"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.IDENTIFIER)

    def test_tokenize_identifier_phrase_upper(self):
        expression = "ABC"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.IDENTIFIER)

    def test_tokenize_identifier_phrase_mixed_lower(self):
        expression = "aBcDEfGHI"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.IDENTIFIER)

    def test_tokenize_identifier_phrase_mixed_upper(self):
        expression = "AbCdEFGhIjk"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.IDENTIFIER)

    def test_tokenize_identifier_phrase_digits_also_mixed(self):
        expression = "aB123cD45efG"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.IDENTIFIER)

    def test_tokenize_operator_lt(self):
        expression = "<"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.LESS_THAN)

    def test_tokenize_operator_lt_eq(self):
        expression = "<="
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.LESS_EQ_THAN)

    def test_tokenize_operator_gt(self):
        expression = ">"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.GREATER_THAN)

    def test_tokenize_operator_gt_eq(self):
        expression = ">="
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.GREATER_EQ_THAN)

    def test_tokenize_operator_eq(self):
        expression = "="
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.EQUALS)

    def test_tokenize_operator_not_eq(self):
        expression = "!="
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.NOT_EQUALS)

    def test_tokenize_operator_and(self):
        expression = "y"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.AND)

    def test_tokenize_operator_or(self):
        expression = "o"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.OR)

    def test_tokenize_apostrophe(self):
        expression = "'"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.APOSTROPHE)

    def test_tokenize_open_par(self):
        expression = "("
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.OPENPAR)

    def test_tokenize_close_par(self):
        expression = ")"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, ttypes.CLOSEPAR)

    def test_tokenize_several_tokens_no_space(self):
        expression = "(foo)"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 3)

    def test_tokenize_several_tokens_space(self):
        expression = "( foo )"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 3)

    def test_tokenize_several_tokens_several_spaces(self):
        expression = "( foo    )"
        tokens = Lexer(expression).tokenize()
        self.assertEqual(len(tokens), 3)