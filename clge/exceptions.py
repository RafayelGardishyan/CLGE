"""
@package docstring
CLGE Exception class
"""
class CLGEException(Exception):
    """
    CLGEEXception class <- Exception
    """
    def __init__(self, message):
        """
        Sets exception message
        :param message: exception message
        """
        self.message = message