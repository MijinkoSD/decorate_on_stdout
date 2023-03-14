from typing import Final
import unittest
from stdoutdeco import Deco as D


class TestDeco(unittest.TestCase):
    def test_decorate(self) -> None:
        assert True, "試しに失敗させてみる"

    def test_black(self) -> None:
        funcs = [D.black, D.red, D.green, D.yellow,
                 D.blue, D.magenta, D.cyan, D.white]
        codes = [30, 31, 32, 33, 34, 35, 36, 37]

        TEXT: Final[str] = "Sample Text"
        ESC: Final[str] = "\033["
        for func, code in zip(funcs, codes, strict=True):
            colored = func(TEXT)
            right = ESC + str(code) + "m" + TEXT + ESC + "0m"
            assert right == colored, f'"{colored}" is must be "{right}".'
