# 2. The Pipline Design

## Overview

This proposal focus on the design and implementation of the pipline.

## Assumption

Current proposal assumes the statement can be constucted by:

```python
new_statement = statement(statement_str=input_str)
```
where `new_statement` is a statement type, 
and the `input_str` is the literal string of the statement

and the evaluation of the statement can be done via:

```python
statement_eval = statement.eval()
```
`statement_eval` is a python statement that can be evaluated via `eval` function in python.

**For more information on Parsing a statement, see SYEMATICS proposal for more.**


## Pipline Stack

Pipline is handled via a stack.

``` python
pipline_stack = input_str.split(const.PIPLINE_STR)
pipline_stack.reverse()
```

where `input_str` is the input string.
`const.PIPLINE_STR` is a string that represent the pipline, currently determined to be `"|"`.
`pipline_stack` is the stack that manages the statements.


## Getting a Statement

Each string between two pipline is called a `statement`.

each statement can be gotten via the following command:

```python
new_statement = pipline_stack.pop()
```

## Handle the Pipline Stack


There are three cases for getting a statement:

### Empty `pipline_stack`

```python
if (!pipline_stack):
    return pre_statement_eval
```

### The First Statement

The first statement is the statement where no input is piped to.

Example:

```bash
1 + 2 | $_ + 3
```

`1 + 2` is the first statement, and it's result is piped to `$_ + 3`

#### How to Check

This is done by checking whether the `previeous_statement_eval` is `null`.

For evaluating statemnt, see SYEMATICS proposal for more.

#### How to Handle

This statement will be handled by the following code.

```python
cur_statement_str = pipline_stack.pop()
cur_statement = statement(statement_str=cur_statement_str)
pre_statement_eval = cur_statement.eval()
```


### The Other Statement

The other statement refers to a statement that is behind at least one `PIPLINE_STR`.

#### How to Check

This can be checked by `pre_statement_eval` is not equal to `null`.

For evaluating statemnt, see SYEMATICS proposal for more.

#### How to Handle

There are 3 cases in this problem:
- if there exists `$_` in a non-string context, replace it with `pre_statement_eval`
- if there this command if registered with pipline via `add_pipline` command with long name `long_para_name`, 
    add `--long_para_name previeous_statement_eval` to the end of `statement_str`
- else we will add that to the first positional parameter.

This statement will be handled by the following code.

```python
cur_statement_str = pipline_stack.pop()
statement = statement(pip_statement_str=cur_statement_str, piped_str=pre_statement_eval)
pre_statement_eval = cur_statement.eval()
```

the pipline will be handled during the construction of the statement.

