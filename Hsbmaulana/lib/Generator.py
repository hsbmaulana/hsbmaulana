from enum import Enum
from random import choice

class Generator:

    class Type (Enum):

        """ :*: Type """
        BINARY, OCTAL, DECIMAL, HEXADECIMAL = [2, 8, 10, 16]

    def generate (self, length: int, kind: Type = Type.DECIMAL) -> str:
        """
        :type length: int
        :type kind: Type = Type.DECIMAL
        :rtype: str
        """
        id = choice (range (1, length + 1)) - 1

        if kind == self.Type.BINARY:

            return str (bin (id)).replace ("0b", "")

        elif kind == self.Type.OCTAL:

            return str (oct (id)).replace ("0o", "")

        elif kind == self.Type.DECIMAL:

            return str (int (id)).replace ("", "")

        elif kind == self.Type.HEXADECIMAL:

            return str (hex (id)).replace ("0x", "")