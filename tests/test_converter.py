import pytest

from base64converter.back import Converter


def test_decoder_encode():
    x: str = "This is a test string."
    expected: str = "VGhpcyBpcyBhIHRlc3Qgc3RyaW5nLg=="
    result: str = Converter.encode(x)

    assert expected == result

def test_decoder_decode():
    x: str = "VGhpcyBpcyBhIHRlc3Qgc3RyaW5nLg=="
    expected: str = "This is a test string."
    result: str = Converter.decode(x)

    assert expected == result

