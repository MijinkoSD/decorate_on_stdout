# 開発時の覚え書き

## 使用している開発環境
- Windows 11
- VSCode
- Python 3.11
  - Microsoft Storeから取得したやつ
  - 複数のバージョンを同時に入れている場合は、
    CLIでの実行時に`python`, `pip`ではなく`python3.11`, `pip3.11`
    と入力しなければならないことがあります


## コードのチェック・フォーマットに使用しているもの
- mypy
  - 型チェック
- unittest
  - テストランナー
- flake8
  - PEP 8 に準拠しているかをチェック
- autopep8
  - オートフォーマッタ


### インストールコマンド

```bash
pip install -U pip
pip install -U mypy flake8 autopep8
```

### 使い方
[code_test.yml](/.github/workflows/code_test.yml)を漁ってください。


## パッケージの生成に使用しているもの
- build
  - pyproject.tomlを使用したパッケージビルディング
- setuptools
  - `setup.cfg`を使用したパッケージの定義に必要なツール


### インストールコマンド

```bash
pip install -U pip
pip install -U mypy flake8 autopep8
```

### 使い方
```bash
python -m build
```

パッケージ生成に成功すれば、`dist/`ディレクトリに`.tar.gz`形式のファイルが生成されます。


### 開発中のパッケージのインストール方法

パッケージ生成が済んでいるのなら、
```bash
pip install --force-reinstall <ファイル>
```
でインストールできたはずです。

リモートリポジトリに上げたものを使用するのであれば、
```bash
pip install --force-reinstall git+https://github.com/MijinkoSD/stdoutdeco.git@<ブランチ名>
```
を使用してください。
