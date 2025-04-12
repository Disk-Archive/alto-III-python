import typing


class ErrorCheck(object):
    def __init__(self):
        pass

    def __call__(self, fn: typing.Callable) -> str:

        alto_result = fn()

        parts = alto_result.split("|")

        if len(parts) <= 1:
            raise AltoException("Unrecognised alto message")

        if parts[0] == "0":
            raise AltoException("Alto returned a zero error code")

        return " ".join(parts[1:])


class AltoException(Exception):
    pass


