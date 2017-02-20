from typing import List

from scr.helpers.general_function import *
from scr.helpers.variable import *
from scr.parsers.helper_model import *
from scr.pipline import pipline_helper


class Statement:
    def __init__(self, statement_str: str, pipline_value: object = None):
        """
        this is the constructor of the statement class
        statement class has the following property:
        __STATEMENT_STR__:
            read only constant keep track of the original statement string
        __pipline_value__:
            a python object is the value that get piped in this statement
        __evaled_statement_str__:
            the evaluated document string,
            this is a variable that changes while we parse
        __para__:
            a list of parameter type indicates the parameter of the command,
            only applicable when parse as python in shell syntax
        __parse_failures__:
            a list of ParseFailure type to indicate how they failed

        :param statement_str: the input of statement str
        :param pipline_value: the input of pipline value
        """
        self.__STATEMENT_STR__ = statement_str
        self.__pipline_value__ = pipline_value
        self.__evaled_statement_str__ = statement_str.strip()
        self.__para__ = []
        self.__parse_failures__ = []
        self.__embedded_structures__ = []

    @property
    def parse_failures(self) -> List[ParseFailure]:
        """
        property of __parse_failures__
        :return: the content of __parse_failures__
        """
        return self.__parse_failures__

    @property
    def embedded_structures(self) -> List[EmbeddedStructure]:
        """
        property of __embedded_structures__
        :return: content of __embedded_structures__
        """
        return self.__embedded_structures__

    @property
    def orig_statement_str(self) -> str:
        """
        the property of original statement str
        :return: the content of __STATEMENT_STR__
        """
        return self.__STATEMENT_STR__

    @property
    def command(self) -> str:
        """
        return the first element of original statement str
        only applicable when parse as shell statement or python in shell syntax
        :return: the command name
        """
        return self.orig_statement_str.split()[0]

    def __handle_pipline__(self):
        """
        this method handles pipline by converting it into an embedded grammar.
        there are three cases:
        1. uses PIPLINE_VALUE_PLACEHOLDER:
            replace the PIPLINE_VALUE_PLACEHOLDER with the pipline_value
        2. there is a registered parameter that takes pipline:
            add the parameter name and pipline_value at the end
        3. if there is non of above:
            add the pipline_value to the first position as positional parameter
        """
        # first case there is a pipline value placeholder
        if not_in_string_context(
                substring=PIPLINE_VALUE_PLACEHOLDER,
                statement_string=self.__evaled_statement_str__):

            self.__evaled_statement_str__ = \
                self.__evaled_statement_str__.replace(
                    PIPLINE_VALUE_PLACEHOLDER,
                    "{0}(self.__pipline_value__)".format(EMBED_MARKER))

        # second case need to find the command's pipline parameter
        else:
            self.__command__ = self.command  # the first word

            # using pipline parameter is
            # not supported in python statement and empty statement
            self.__parse_failures__.append(
                ParseFailure(parse_method=ParseMethod.empty_statement,
                             failure_type="PipLineError",
                             failure_message=PIPLINE_ERROR_MESSAGE_EMPTY))

            self.__parse_failures__.append(
                ParseFailure(parse_method=ParseMethod.python_statement,
                             failure_type="PipLineError",
                             failure_message=PIPLINE_ERROR_MESSAGE_PYTHON))

            try:
                # try to find the data base to get the registered pipline name
                para_name, is_long_name = pipline_helper.get_pipline_para_name(
                    command=self.__command__)

                if is_long_name:
                    # if we got the long parameter name
                    self.__evaled_statement_str__ += "--{0} {1}".format(
                        para_name,
                        "{0}(self.__pipline_value__)".format(EMBED_MARKER))

                else:
                    # if we got the short parameter name
                    self.__evaled_statement_str__ += "-{0} {1}".format(
                        para_name,
                        "{0}(self.__pipline_value__)".format(EMBED_MARKER))

            except Exception as e:
                # uses positional parameter
                arg_list = self.__evaled_statement_str__.split()
                # insert the pipline value using embedded grammar
                arg_list.insert(
                    1,
                    "{0}(self.__pipline_value__)".format(EMBED_MARKER))

                self.__evaled_statement_str__ = " ".join(arg_list)

    def __find_embedded_structure__(self):
        raise NotImplementedError
