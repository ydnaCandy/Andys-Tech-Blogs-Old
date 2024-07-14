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
ローカルPC側で鍵を作成

```bash
$ ssh-keygen -t ed25519

# 変更しない場合はEnter
>>> Enter file in which to save the key:

# パスフレーズを作成する場合は入力
>>> Enter passphrase (empty for no passphrase): 
>>> Enter same passphrase again:

# サーバー側に公開鍵をコピー
$ scp id_ed25519.pub [goku]@[Host IP]:/home/[user_name]/.ssh/

```

Ubuntu側で設定

```bash
# 公開鍵を登録
$ cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys

# ファイルの権限を変更
$ chmod 600 ~/.ssh/authorized_keys

# サービス再起動
$ sudo systemctl restart ssh
```

### IP固定

```bash
$ sudo nano /etc/netplan/99-custom.yaml 
```

```yaml
network:
  version: 2
    wifis:
      wlan0:
        dhcp4: false
        addresses: [IP_Address/24]
        routes:
          - to: default
            via: [default gateway]
        nameservers:
        addresses: [DNS_IP, 8.8.8.8]
        optional: true
        access-points:
          "[ssid_name]":
            auth:
              password: "[password]"
```

### Autologin

```bash
$ sudo nano /etc/gdm3/custom.conf
```

```conf
# Enabling automatic login
#  AutomaticLoginEnable = true
#  AutomaticLogin = user1

# Enabling automatic login
AutomaticLoginEnable = true
AutomaticLogin = [username]
```

```bash
$ sudo reboot now
```

再起動後、自動ログインされれば成功

## 参考
- https://tenteroring.org/sierra/?p=3605