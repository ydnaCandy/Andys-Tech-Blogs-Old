# python環境構築



## 実施日

2021/09/04



## 環境

- PC
  - MacBook Pro 2017

- OS

  - macOS Big Sur

  



## homebrewのインストール

```bash
$ brew -v
>>> -bash: brew: command not found

$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

$ brew -v
>>> Homebrew 3.2.10
```



### pyenvのインストール

```bash
$ pyenv -v
-bash: /usr/local/bin/pyenv: No such file or directory

$ brew install pyenv

$ pyenv -v
>>> pyenv 2.0.6

$ echo $SHELL
```



### パスを通す

```bash
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

$ source ~/.bash_profile
```



```bash
$ nano ~/.profile
# 下記内容を追記
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

$ source ~/.profile
```

## tkinterを使うことを見越して設定する

```bash
$ pyenv global system

# system以外が表示されたらアンインストールする
$ pyenv versions
* system
  3.X.X (set by /Users/myname/.pyenv/version)

# 
$ pyenv uninstall 3.X.X
```

### tcl-tkのインストール

```bash
$ brew install tcl-tk
tcl-tk is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have tcl-tk first in your PATH, run:
  echo 'export PATH="/usr/local/opt/tcl-tk/bin:$PATH"' >> /Users/[user_name]]/.bash_profile

For compilers to find tcl-tk you may need to set:
  export LDFLAGS="-L/usr/local/opt/tcl-tk/lib"
  export CPPFLAGS="-I/usr/local/opt/tcl-tk/include"

For pkg-config to find tcl-tk you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/tcl-tk/lib/pkgconfig"
```

ターミナルに表示された内容に沿ってパスを通す。

```bash
$ nano ~/.bash_profile
export PATH="/usr/local/opt/tcl-tk/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/tcl-tk/lib"
export CPPFLAGS="-I/usr/local/opt/tcl-tk/include"
export PKG_CONFIG_PATH="/usr/local/opt/tcl-tk/lib/pkgconfig"
```

## pythonのインストール

tkinterを使うために以下のコマンドを実行

```bash
$ PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I/usr/local/opt/tcl-tk/include' --with-tcltk-libs='-L/usr/local/opt/tcl-tk/lib -ltcl8.6 -ltk8.6'" pyenv install 3.8.5
```

```bash 
$ pyenv versions
* system
  3.8.5

$ pyenv global 3.8.5
 
$ pyenv versions
system
* 3.8.5
```

```bash
$ python --version
>>> Python 3.8.5
```



## Jupyter labのインストール

```bash
$ pip --version
>>> pip 20.1.1

$ pip install jupyterlab
```

### node.jsをインストール

```bash
$ brew install nodebrew

$ nodebrew -V
>>> nodebrew use v8.9.4

$ nodebrew ls-remote

$ nodebrew install-binary latest

$ node -v
>>> v14.17.1
```



### 起動確認

任意のフォルダ下でjupyterlabを起動するコマンドを実行して、ブラウザに表示されることを確認する。

```bash
$ jupyter lab
```



## 仮想環境の環境構築

### pipenvの構築

```bash
$ brew install pipenv

$ pipenv --version
>>> pipenv, version 2021.5.29
```

### pipenvを使う

```bash
$ mkdir pipenv_test
$ cd pipenv_test/

# 開発フォルダ内で仮想環境フォルダを作成する設定
$ export PIPENV_VENV_IN_PROJECT=1

$ pipenv --python 3.8.5
>>> Creating a Pipfile for this project...

$ cat Pipfile
>>> [[source]]
>>> url = "https://pypi.org/simple"
>>> verify_ssl = true
>>> name = "pypi"
>>> 
>>> [packages]
>>> 
>>> [dev-packages]
>>> 
>>> [requires]
>>> python_version = "3.8"

# 仮想環境の起動
$ pipenv shell
(pipenv_test) bash-3.2$

# バージョン確認
(pipenv_test) bash-3.2$ python --version
>>> Python 3.8.5

# 仮想環境を停止
(pipenv_test) bash-3.2$ exit
>>> $
```



## パッケージのインストール

使いそうなパッケージをインストールしておく

```bash
$ pip install wheel
$ pip install pandas
$ pip install numpy
$ pip install matplotlib
$ pip install seaborn

```

