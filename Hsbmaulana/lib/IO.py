from typing import Union, List
from os.path import dirname, realpath, abspath
from re import sub

class IO:

    def replace (self, path: str, *args: List[Union[int, str]]) -> None:
        """
        :type path: str
        :type *args: List[Union[int, str]]
        :rtype: None
        """
        try:

            root = "/../../"
            path = abspath (dirname (realpath (__file__))+root+path)

            datas = []

            with open (path, "r") as infile:

                datas = infile.read ().splitlines ()
                infile.close ()

            for arg in args:

                line, search, replace = arg

                datas[line - 1] = sub (search, replace, datas[line - 1], 1)

            with open (path, "w") as outfile:

                outfile.write ("\n".join (datas))
                outfile.close ()

        except IOError as thrower:

            raise Exception (thrower)