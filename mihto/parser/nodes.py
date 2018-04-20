import mihto.lexer.token_types as ttypes


class ExpressionNode:
    __slots__ = ('value1', 'operator', 'value2')
    _pretty_ops = {ttypes.LESS_EQ_THAN: '<=', ttypes.LESS_THAN: '<',
                   ttypes.GREATER_EQ_THAN: '>=', ttypes.GREATER_THAN: '>',
                   ttypes.EQUALS: '=', ttypes.NOT_EQUALS: '!=', ttypes.AND: 'and', ttypes.OR: 'or'}

    def __init__(self, value1, operator, value2):
        self.value1 = value1
        self.operator = operator
        self.value2 = value2

    def __repr__(self):
        return "<Expression '{} {} {}' >".format(repr(self.value1), repr(self.operator), repr(self.value2))

    def __str__(self):
        return "{} {} {}".format(str(self.value1), self._pretty_ops[self.operator], str(self.value2))


class ValueNode:
    __slots__ = ('value',)
    __nodetype__ = 'valuenode'

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "<{} {} >".format(self.__nodetype__, self.value)

    def __str__(self):
        return "{}".format(self.value)


class FloatNode(ValueNode):
    __nodetype__ = "Float"

    def __init__(self, value: float):
        super().__init__(value)


class IntegerNode(ValueNode):
    __nodetype__ = "Integer"

    def __init__(self, value: int):
        super().__init__(value)


class VarRefNode(ValueNode):
    __nodetype__ = "VarRef"

    def __init__(self, value: str):
        super().__init__(value)
