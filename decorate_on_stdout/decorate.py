

from typing import Callable, ParamSpec

P = ParamSpec("P")

class Deco:
    @staticmethod
    def __deco(func: Callable[P, tuple[str, str]]) -> Callable[P, str]:
        ESC = "\033["
        def set_arg(*args: P.args, **kwargs: P.kwargs) -> str:
            text, color = func(*args, **kwargs)
            return ESC + color + text + ESC + "0m"
        return set_arg
    
    @staticmethod
    @__deco
    def black(text: str): return text, "30m"
    @staticmethod
    @__deco
    def red(text: str): return text, "31m"
    @staticmethod
    @__deco
    def green(text: str): return text, "32m"
    @staticmethod
    @__deco
    def yellow(text: str): return text, "33m"
    @staticmethod
    @__deco
    def blue(text: str): return text, "34m"
    @staticmethod
    @__deco
    def magenta(text: str): return text, "35m"
    @staticmethod
    @__deco
    def cyan(text: str): return text, "36m"
    @staticmethod
    @__deco
    def white(text: str): return text, "37m"
    # @__deco
    # def color_code(text: str, color: int): return text, color


if __name__ == "__main__":
    # ぶっちゃけここはテストコードとして分割すべき
    print("sample text is below:")
    print(f'{Deco.red("R")}{Deco.green("A")}{Deco.yellow("I")}{Deco.blue("N")}{Deco.magenta("B")}{Deco.cyan("O")}{Deco.white("W")}')
