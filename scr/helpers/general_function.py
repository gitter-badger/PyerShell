import re


def to_bash_str(python_object: object) -> str:
    """
    convert a python object to bash
    this is used when you want to embed other statement in shell statement
    :param python_object: the input python object
    :return: the corresponding string
    """

    if isinstance(python_object, list):
        # if it is a list, join them via space

        return " ".join([to_bash_str(element) for element in python_object])

    elif isinstance(python_object, str):
        # if the object is an string
        # wrap it with quotes

        return '"{0}"'.format(python_object)

    elif isinstance(python_object, type(None)):
        # returns empty string if it is a none type

        return ""

    else:
        # else simply return the str

        return str(python_object)


def not_in_string_context(substring: str, statement_string: str) -> bool:
    """
    this function is to determine whether a substring is in string context
    :param substring: the substring you want to find in the statement string
    :param statement_string: the whole statement string
    :return: whether the substring is not in a string context of statement_str.
             There will be two cases this function is eval to True:
              1. the substring is not in statement string at all
              2. the substring exists in a string context
    """
    # this is the regex to match a string in a statement string
    string_regex = r'(?<!\\)[\"\'].*?(?<!\\)[\"\']'

    # remove all the strings in statement_string
    clean_statement_strings = re.sub(pattern=string_regex,
                                     repl="",
                                     string=statement_string)

    # see if the substring still exists
    return substring in clean_statement_strings
