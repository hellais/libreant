class WebAntException(Exception):
    pass


class InvalidCapability(WebAntException):
    def __init__(self, cap_name):
        self.message = "Invalid capability: %s" % cap_name
