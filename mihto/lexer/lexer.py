import re

from mihto.lexer.token_types import TOKEN_PATTERNS


class Lexer:

    def __init__(self, code):
        self.code = code

    def tokenize(self):
        tokens = []
        while self.code:
            tokens.append(self.single_tokenize())
            self.code = self.code.strip()
        return tokens

    def single_tokenize(self):
        for token_type, regex in TOKEN_PATTERNS:
            regex = re.compile(r'\A({})'.format(regex))
            value = regex.search(self.code)
            if value:
                value = value.group(0)
                self.code = self.code[len(value):]
                return Token(token_type, value)

        raise RuntimeError("Couldn't match token on {}".format(self.code))


class Token:
    __slots__ = ('type', 'value')

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return "<Token type={}, value={} >".format(self.type, self.value)