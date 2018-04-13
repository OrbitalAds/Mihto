import mihto.lexer.token_types as ttypes
class ExpressionNode:
    __slots__ = ('value1', 'operator', 'value2')
    _pretty_ops = {ttypes.LESS_EQ_THAN : '<=', ttypes.LESS_THAN : '<',
                   ttypes.GREATER_EQ_THAN : '>=', ttypes.GREATER_THAN : '>',
                   ttypes.EQUALS : '=', ttypes.NOT_EQUALS: '!=', ttypes.AND : 'and', ttypes.OR: 'or'}

    def __init__(self, value1, operator, value2):
        self.value1 = value1
        self.operator = operator
        self.value2 = value2

    def __repr__(self):
        return "<Expression '{} {} {}' >".format(repr(self.value1), repr(self.operator), repr(self.value2))

    def __str__(self):
        return "{} {} {}".format(str(self.value1), self._pretty_ops[self.operator], str(self.value2))


class FloatNode:
    __slots__ = ('value', )

    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return "<Integer {} >".format(self.value)

    def __str__(self):
        return "{}".format(self.value)

class IntegerNode:
    __slots__ = ('value', )

    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return "<Integer {} >".format(self.value)

    def __str__(self):
        return "{}".format(self.value)

class VarRefNode:
    __slots__ = ('value', )

    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return "<Var Ref {} >".format(self.value)

    def __str__(self):
        return "{}".format(self.value)