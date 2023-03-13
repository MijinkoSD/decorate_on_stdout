# stdout上で文字装飾できるようにするやつ
- 個人的に必要になって作っただけなので機能は最小限です。
  - まだ文字色を変えるコードしか書いていない
- 多機能なのが欲しい人は他のリポジトリを漁りましょう。

## インストール
シェル上でこのコマンドを入力してください。

```bash
pip3 install -U git+https://github.com/MijinkoSD/stdoutdeco.git
```

## 使い方
先に述べた通り、文字色を変えることしかできません。

```py
from stdoutdeco import Deco

print(Deco.red("RED TEXT"))
# 赤い文字でRED TEXTと表示される
```

色は`black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`の8色です。
