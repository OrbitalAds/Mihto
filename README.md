# Mihto language

## What is it?

Mihto (Spanish pronunciation: [mĩʃt̪o]) is an evaluation language made by [JavierLuna](https://github.com/JavierLuna/mihto) while trying to figure out how compilers and interpreters work.

Basically it reads and evaluates an expression (or chain of expressions) 

The project will be up in Pypi soon and will follow the versioning convention,
using MAJOR.MINOR.PATCH format. A bump in the PATCH part will not mean API breakage, but a bump in MAJOR or MINOR might.

## Syntax

* Types:
    * Variables: Variables you can define in the env of the Evaluator (or the Mihto class). Example: `var`, `Evaluator({'var': 3})`
    * Integers: Your old and trusty integer. `42`
    * Floats: Like more precise integers. `42.34`
    * Comparison operators: Turn values into boolean expressions!. `<`, `<=`, `>`, `>=`, `=`, `!=`
    * Logical operators: Link boolean expressions into one single boolean expression!. `y`. `o`
    * Parenthesis: Gotta prioritize them operations. `(`, `)

* Examples: `Evaluator({'var' : 3, 'var2': 3}).evaluate(expression)`
    * expression = `1 < var` -> True
    * expression = `1 < var <= 42` -> True
    * expression = `1 < var y var2 > 43` -> False
    * expression = `1 > var o (1 < var y 3 <= var2 < 43)` -> True

## How to use it in your python code

You can use the language directly or the facade created for the Discriminator, it doesn't really matter.

Through Mihto:
`result = Mihto({'a': 2}).evaluate("1 = a")`

Cool, uh?
