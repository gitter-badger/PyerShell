import scr.helpers.general_function as gf


class TestToBashStr:

    def test_str(self):
        """
        test for string object
        """
        assert gf.to_bash_str(python_object="test") == '"test"'

    def test_num(self):
        """
        test for numeric object
        """
        assert gf.to_bash_str(python_object=1) == '1'

    def test_none(self):
        """
        test for none object
        """
        assert gf.to_bash_str(python_object=None) == ""


    def test_list(self):
        """
        test for complex list structure
        """
        assert gf.to_bash_str([1, "test", [1, None]]) == '1 "test" 1 '
