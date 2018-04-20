LESS_EQ_THAN = 'less_eq_than'
GREATER_EQ_THAN = 'greater_eq_than'
LESS_THAN = 'less_than'
GREATER_THAN = 'greater_than'
EQUALS = 'equals'
NOT_EQUALS = 'not_equals'
AND = 'and'
OR = 'or'
IDENTIFIER = 'identifier'
FLOAT = 'float'
INTEGER = 'integer'
OPENPAR = 'openpar'
CLOSEPAR = 'closepar'


TOKEN_PATTERNS = [
    [LESS_EQ_THAN, r"<="],
    [GREATER_EQ_THAN, r">="],
    [LESS_THAN, r"<"],
    [GREATER_THAN, r">"],
    [NOT_EQUALS, r"!="],
    [EQUALS, r"="],
    [AND, r"y"],
    [OR, r"o"],
    [IDENTIFIER, r"[a-zA-Z]+"],
    [FLOAT, r"\d+\.\d+"],
    [INTEGER, r"\d+"],
    [OPENPAR, r"\("],
    [CLOSEPAR, r"\)"]
]

OPERATORS = [LESS_EQ_THAN, LESS_THAN, GREATER_EQ_THAN, GREATER_THAN, EQUALS, NOT_EQUALS]
LOGICAL_OPERATORS = [AND, OR]