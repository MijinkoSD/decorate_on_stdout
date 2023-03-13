import sys
from asyncio import sleep, run, gather

ESC = "\033["


class Line:
    def __init__(self, multi_line, text: str = ""):
        self.multi_line = multi_line
        self.text = text

    # def __del__(self):
    #     self.multi_line.remove_line(line=self)

    async def update(self, text: str):
        """ 表示内容を更新します """
        self.text = text
        await self.multi_line.update_line(text=text, line=self)
    
    async def remove(self):
        """ 行を削除します """
        await self.multi_line.remove_line(self)
        del self

class MultiLine:
    def __init__(self):
        """ コンソールテキストの複数行の更新をサポートします。 """
        self.lines: list[_Line] = []
        """ 行ごとのインスタンス。添字が若いほど上の行。 """
        self.allow_remove_line = True
        """ 行の削除を許可するか """

    def __del__(self):
        self.allow_remove_line = False

    async def add_line(self, text: str = "") -> Line:
        """ 表示する行を下に追加します。 """
        line = Line(self, text=text)
        self.lines.append(line)
        sys.stdout.write("\n" + text)
        return line

    async def update_line(self, text: str, line: Line) -> None:
        try:
            index = self.lines.index(line)
        except IndexError:
            return
        
        count = len(self.lines)
        move_len = count - index - 1
        self._cursor_up(move_len)
        self._render_cursor_line(text)
        self._cursor_down(move_len)

        bottom_line_text = self.lines[-1].text
        self._render_cursor_line(bottom_line_text)

    async def remove_line(self, line: Line) -> None:
        """ 行を削除します。 """
        if not self.allow_remove_line: return
        try:
            index = self.lines.index(line)
        except IndexError:
            return
        
        count = len(self.lines)
        move_len_min = count - index - 1
        self._cursor_up(move_len_min)
        for i in range(index - 1, -1, -1):
            self._render_cursor_line(self.lines[i].text)
            self._cursor_up(1)
        self._render_cursor_line("")
        self._cursor_down(count - 1)
        bottom_line_text = self.lines[-1].text
        self._render_cursor_line(bottom_line_text)

        self.lines.pop(index)

    @staticmethod
    def _cursor_up(count: int) -> None:
        if count <= 0: return
        sys.stdout.write(f"{ESC}{count}F")

    @staticmethod
    def _cursor_down(count: int) -> None:
        if count <= 0: return
        sys.stdout.write(f"{ESC}{count}E")

    @staticmethod
    def _render_cursor_line(text: str) -> None:
        sys.stdout.write(f"{ESC}2K")
        sys.stdout.write("\r" + text)


async def _main():
    """ 本来ここに書くべきではないが、面倒くさかったので…（後で消す） """

    m = MultiLine()
    yet = []
    l1 = await m.add_line("sample1")
    l2 = await m.add_line("sample2")
    l3 = await m.add_line("sample3")
    l4 = await m.add_line("sample4")
    await sleep(0.5)
    yet.append(l2.update("oooo"))
    await sleep(0.5)
    for i in range(200):
        await gather(
            l2.update(str(i)),
            l3.update(str(i))
            )
        await sleep(0.0001)
    await sleep(0.5)
    # await l2.remove()
    await sleep(0.5)
    await l3.update("sample?")
    await sleep(0.5)

    await gather(*yet)

if __name__ == "__main__":
    # TODO: テストコードとして分割する

    run(_main())
