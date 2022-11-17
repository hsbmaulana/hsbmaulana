#!/usr/bin/env python3

from .src.Emoji import Emoji
from .src.Clock import Clock
from .lib.IO import IO

if __name__ == "__main__":

    emoji = str (Emoji ())
    clock = str (Clock ())

    IO ().replace ("README.md", [1, r"(?<=Hi\s)([\S])", emoji], [2, r"([0-9]+)(?=\shours)", clock])