

class Deco:
    def __deco(func) -> str:
        ESC = "\033["
        def set_arg(*args, **kwargs):
            text, color = func(*args, **kwargs)
            return ESC + color + text + ESC + "0m"
        return set_arg
    
    @__deco
    def black(text: str): return text, "30m"
    @__deco
    def red(text: str): return text, "31m"
    @__deco
    def green(text: str): return text, "32m"
    @__deco
    def yellow(text: str): return text, "33m"
    @__deco
    def blue(text: str): return text, "34m"
    @__deco
    def magenta(text: str): return text, "35m"
    @__deco
    def cyan(text: str): return text, "36m"
    @__deco
    def white(text: str): return text, "37m"
    @__deco
    def color_code(text: str, color: int): return text, "37m"


if __name__ == "__main__":
    # ぶっちゃけここはテストコードとして分割すべき
    print("sample text is below:")
    print(f'{Deco.red("R")}{Deco.green("A")}{Deco.yellow("I")}{Deco.blue("N")}{Deco.magenta("B")}{Deco.cyan("O")}{Deco.white("W")}')
