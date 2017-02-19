
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
