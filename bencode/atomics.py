import re


class DecodeException(Exception):
    pass


class IntegerDecodeError(DecodeException):
    pass


class IntegerManager:
    expression = re.compile(r"^i(-?\d+)e$")

    @classmethod
    def encode(cls, r: int):
        return b'i' + str(r).encode() + b'e'

    @classmethod
    def decode(cls, r: bytes):
        result = cls.expression.match(r.decode())

        if result:
            try:
                return int(result.group(1))
            except IndexError as e:
                raise IntegerDecodeError() from e
