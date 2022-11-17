from .Contracts.Stringable import Stringable
from ..lib.Generator import Generator

class Emoji (Stringable):

    def __init__ (self) -> None:
        """
        :rtype: None
        """

        """ :__smiles: List[str] """
        self.__smiles = [

            "60", "61", "62", "63", "64",
            "91", "92", "93"
        ]

    def __str__ (self) -> str:
        """
        :rtype: str
        """

        generator = Generator ()

        form = "utf-8"
        prefix = "1f" # "0001f" #
        suffix = self.__smiles[int (generator.generate (len (self.__smiles)))]
        postfix = generator.generate (Generator.Type.HEXADECIMAL.value, Generator.Type.HEXADECIMAL)

        emoji = chr (int (prefix+suffix+postfix, Generator.Type.HEXADECIMAL.value)).encode (form).decode (form)

        return emoji