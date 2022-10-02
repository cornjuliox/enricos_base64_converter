from base64 import urlsafe_b64decode, urlsafe_b64encode
from typing import Callable


class Converter():
    @classmethod
    def __perform(cls, text: str, op: Callable[[bytes], bytes], encoding: str="utf-8"):
        str_bytes: bytes = bytes(text, encoding)
        en_de_coded: bytes = op(str_bytes)
        result: str = en_de_coded.decode(encoding)
        return result

    @classmethod
    def encode(cls, text: str, encoding="utf-8") -> str:
        return cls.__perform(text, urlsafe_b64encode, encoding)

    @classmethod
    def decode(cls, text: str, encoding="utf-8") -> str:
        return cls.__perform(text, urlsafe_b64decode, encoding)
