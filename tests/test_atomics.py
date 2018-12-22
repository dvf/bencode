import pytest

from bencode.atomics import IntegerManager


@pytest.mark.parametrize("encoded_integer, decoded_integer", [
    (b"i200e", 200),
    (b"i0e", 0),
    (b"i-1e", -1),
    (b"i-100e", -100),
])
def test_integer_decode(encoded_integer, decoded_integer):
    i = IntegerManager()

    decoded = i.decode(encoded_integer)
    assert decoded == decoded_integer
