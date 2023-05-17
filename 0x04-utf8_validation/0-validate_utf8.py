#!/usr/bin/python3
"""ALX Interview Preparation: UTF-8 validation module.
"""


def validUTF8(data):
    """a method that determines if a given
       data set represents a valid UTF-8 encoding
    """
    skip_char = 0
    n = len(data)

    # a for loop that iterates over each element in the data list.
    for i in range(n):

        # If 'skip_char' is greater than 0, it means the current byte
        # is a continuation byte,
        # and we decrement 'skip_char' by 1 and continue to the next iteration.
        # This avoids rechecking bytes that are part of a multibyte character.
        if skip_char > 0:
            skip_char -= 1
            continue

        # determine its UTF-8 encoding validity.
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            skip_char = 0
        elif data[i] & 0b11111000 == 0b11110000:

            # check for 4-byte utf-8 character encoding
            span = 4
            if n - i >= span:
                next_char_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_char_body):
                    return False
                skip_char = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:

            # check for 3-byte utf-8 character encoding
            span = 3
            if n - i >= span:
                next_char_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_char_body):
                    return False
                skip_char = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:

            # check for 2-byte utf-8 character encoding
            span = 2
            if n - i >= span:
                next_char_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_char_body):
                    return False
                skip_char = span - 1
            else:
                return False
        else:
            return False
    return True
