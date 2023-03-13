import unittest
import stdoutdeco.Deco as D


class TestDeco(unittest.TestCase):
    def test_decorate(self):
        assert True, "試しに失敗させてみる"

    def test_black(self):
        funcs = [D.black, D.red, D.green, D.yellow,
                 D.blue, D.magenta, D.cyan, D.white]
        codes = [30, 31, 32, 33, 34, 35, 36, 37]

        text = "Sample Text"
        while func, code in zip(funcs, codes):
            colored = func(code)
