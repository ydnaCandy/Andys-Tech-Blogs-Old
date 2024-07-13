# Ubuntu初期セットアップ手順

## 設定環境
- ハードウェア
    - Raspberry Pi 4
- OS
    - Ubuntu 24.04 Desktop
    - Raspberry Pi imagerからインストール

## 初期設定

### 初回起動

1. WelcomeでEnglishを選択し、continueをクリック

2. keyboard layoutでJapaneseを選択し、continueをクリック

3. Wirelessで。`i don't want to...`を選択し、continueをクリック

4. Where are you?でJapan Timeを選択し、continueをクリック

5. Who are you?でユーザー情報を入力

6. セットアップが始まるので、Applying changeが表示されるまで待つ

7. 再起動が始まり、ログイン画面が表示されるので、ログインする


### ネットワークの設定

- wifiでの設定を想定

```bash
$ cd /etc/netplan

$ sudo mv 50-cloud-init.yaml 50-cloud-init.yaml_bk 

$ sudo cp 50-cloud-init.yaml_bk 99-custom.yaml

$ sudo nano 99-custom.yaml
```


```yaml
network:
  version: 2
  wifis:
    wlan0:
      renderer: NetworkManager
      match: {}
      dhcp4: true
      access-points:
        "[ssid_name]":
          auth:
            password: "[password]"
```


### aptのミラーサイトを変更

```bash
# バックアップとしてコピーしておく
$ sudo cp /etc/apt/sources.list.d/ubuntu.sources /etc/apt/sources.list.d/ubuntu.sources_bk

# 編集
$ sudo nano /etc/apt/sources.list.d/ubuntu.sources
```

```conf
## See the sources.list(5) manual page for further settings.
Types: deb
# portsの前にjp.を追加
URIs: http://jp.ports.ubuntu.com/ubuntu-ports

## Ubuntu security updates. Aside from URIs and Suites,
## this should mirror your choices in the previous section.
Types: deb
# portsの前にjp.を追加
URIs: http://jp.ports.ubuntu.com/ubuntu-ports
```

```bash
# 再起動する
$ sudo reboot now

```


### パッケージのアップデート

```bash
# 日時がずれているとアップデートできないので合わせる
$ sudo date --set='yyyy/mm/dd hh:mm:ss'

$ sudo apt update

$ sudo apt upgrade

$ sudo apt autoremove

$ sudo apt clean

$ sudo reboot now
```


### sshの設定

```bash
$ sudo apt install openssh-server

$ sudo systemctl status ssh

$ sudo systemctl enable ssh

$ sudo nano /etc/ssh/sshd_config

```


### 不要なパッケージの削除

```bash
# 標準ソフト系をアンインストール
sudo apt remove libreoffice*
sudo apt remove thunderbird*
sudo apt remove transmission*
sudo apt remove shotwell
sudo apt remove remmina


sudo apt autoremove -y
```






## 詳細設定


### sshを鍵認証に変更

### 自動ログアウト

### IP固定

### スリープOFF





## 参考
- https://tenteroring.org/sierra/?p=3605