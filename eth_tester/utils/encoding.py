from RAJ1000_utils import (
    int_to_big_endian,
)
from RAJ1000_utils.toolz import (
    compose,
    curry,
)


@curry
def zpad(value, length):
    return value.rjust(length, b"\x00")


zpad32 = zpad(length=32)


int_to_32byte_big_endian = compose(
    zpad32,
    int_to_big_endian,
)
