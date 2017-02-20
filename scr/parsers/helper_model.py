from enum import Enum


class ParseMethod(Enum):
    """"
    this is the class indicates all the parse method
    we try to use to parse a statement
    """
    empty_statement = 0
    python_statement = 1
    python_in_shell_syntax = 2
    shell_statement = 3


class ParseFailure:
    def __init__(self, parse_method: ParseMethod, failure_type: str,
                 failure_message: str):
        """
        this is the class indicates one parse failure
        since we try to parse a statement in four ways,
        therefore four ParseFailure object will be in statement.failure

        :param parse_method: the method we currently using
        :param failure_type:
            the error type of the error encountered when parsing
        :param failure_message:
            the error message of the error encountered when parsing
        """
        self.parse_method = parse_method
        self.failure_type = failure_type
        self.failure_message = failure_message


class EmbeddedStructure:
    def __init__(self, embedded_str: str, embedded_value: object):
        """
        this class keeps track of all the embedded statement in a statement
        notice, pipline is also handled by embedded structure

        :param embedded_str: the string of the embedded structure
        :param embedded_value: the evaluated value of the embedded structure
        """
        self.embedded_str = embedded_str
        self.embedded_value = embedded_value
