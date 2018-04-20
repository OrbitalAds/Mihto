from mihto import Lexer, Parser, Evaluator


class Mihto:

    def __init__(self, env=None):
        self.env = env or {}

    def evaluate(self, expression: str):
        lexer = Lexer(expression)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        expression = parser.parse()
        evaluator = Evaluator(self.env)
        return evaluator.evaluate(expression)
