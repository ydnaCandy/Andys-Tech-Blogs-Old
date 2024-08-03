# venvを使った仮想環境構築

## よくあるディレクトリ構成

```bash

project_root/
├── .venv/
├── src/
├── .gitignore
├── README.md
└──  requirements.txt

```

## 手順

### venv構築コマンド

```bash

# 仮想環境の作成
$ python -m venv .venv

# 仮想環境の起動(mac)
$ source env/bin/activate

# 仮想環境の起動(Windows)
# powershellの実行ポリシーに注意
$ env\Scripts\Activate.ps1

# 仮想環境の停止(mac/windows)
$ deactivate

# ライブラリのインストール
([env]) $ pip install [library]

#  仮想環境のコピー
# 使用しているライブラリ情報を出力
$ pip freeze > requirements.txt

# 新環境側起動後に取り込む
$ pip install -r requirements.txt

```

### .gitignore

```bash

# バーチャル環境
.venv/

# Python 一時ファイル
*.pyc
*.pyo
*.pyd
__pycache__/
*.so

# OSに依存するファイル
.DS_Store
Thumbs.db

# その他
*.egg
*.egg-info/
dist/
build/
```