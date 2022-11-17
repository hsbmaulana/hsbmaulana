from abc import ABC, abstractmethod
from typing import Union, Tuple, Optional, Any, cast

class Stringable (ABC):

    @abstractmethod
    def __str__ (self) -> str:
        """
        :rtype: str
        """
        pass