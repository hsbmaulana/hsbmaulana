from .Contracts.Stringable import Stringable
from ..lib.Generator import Generator
from os import environ
from datetime import datetime

class Clock (Stringable):

    def __str__ (self) -> str:
        """
        :rtype: str
        """
        date = int (environ.get ("BECODER_SINCE_DATE"))
        month = int (environ.get ("BECODER_SINCE_MONTH"))
        year = int (environ.get ("BECODER_SINCE_YEAR"))

        then = datetime (year, month, date)
        now = datetime.now ()

        inaday = int (environ.get ("STUDY_HOURS_IN_A_DAY"))
        duration = inaday * (now - then).days

        clock = str (duration)

        return clock