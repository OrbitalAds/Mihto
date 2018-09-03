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
OPENPAR = 'open_par'
CLOSEPAR = 'close_par'
PLUS =r"plus"
SCORE = "minus"
ASTERISK = "asterisk"
BACKSLASH = "back_slash"

TOKEN_PATTERNS = [
    [LESS_EQ_THAN, r"<="],
    [GREATER_EQ_THAN, r">="],
    [NOT_EQUALS, r"<>"],
    [LESS_THAN, r"<"],
    [GREATER_THAN, r">"],
    [EQUALS, r"="],
    [AND, r"\band\b"],
    [OR, r"\bor\b"],
    [PLUS, r"\+"],
    [SCORE, r"-"],
    [ASTERISK, r"\*"],
    [BACKSLASH, r"\\"],
    [IDENTIFIER, r"\b[a-zA-Z]+([a-zA-Z]|\d|_|\\|-)*\b"],
    [FLOAT, r"\b\d+\.\d+\b"],
    [INTEGER, r"\b\d+\b"],
    [OPENPAR, r"\("],
    [CLOSEPAR, r"\)"]
]

OPERATORS = [LESS_EQ_THAN, LESS_THAN, GREATER_EQ_THAN, GREATER_THAN, EQUALS, NOT_EQUALS]
LOGICAL_OPERATORS = [AND, OR]
