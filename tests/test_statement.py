from scr.parsers.statement import Statement


class TestHandlePipline:
    @staticmethod
    def __handle_pipline_easy__(statement_str: str, pipline_value: object) -> str:
        """
        this is a helper to construct a statement and then run handle_pipline, then get the result
        :param statement_str: the statement string
        :param pipline_value: the value that is piped into the statements
        :return: the evaluated statement string after pipline is handled
        """
        test_statment = Statement(statement_str=statement_str, pipline_value=pipline_value)
        test_statment.__handle_pipline__()
        return test_statment.__evaled_statement_str__

    def test_pipline_marker(self):
        """
        test when people uses PIPLINE_VALUE_PLACEHOLDER
        """
        result = self.__handle_pipline_easy__(statement_str="[$_ + i for i in range(2)]", pipline_value=1)
        assert result == "[$(self.__pipline_value__) + i for i in range(2)]"

    def test_positional_para(self):
        """
        test to handle pipline by add the pipline_value to the first positional parameter
        """
        result = self.__handle_pipline_easy__(statement_str="ls", pipline_value="test/")
        assert result == "ls $(self.__pipline_value__)"

    def test_keyword_para(self):
        pass
