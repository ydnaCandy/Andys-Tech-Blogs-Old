# RPiOS Bookworm初期設定手順


## 基本設定

### ネットワーク設定(WiFi)

```bash

# --askでパスワードを対話形式で入力
$ sudo nmcli dev wifi connect "SSID" --ask

# IPv4固定
$ sudo nmcli connection modify "YOUR_CONNECTION_NAME" ipv4.addresses "192.168.1.100/24"
$ sudo nmcli connection modify "YOUR_CONNECTION_NAME" ipv4.gateway "192.168.1.1"
$ sudo nmcli connection modify "YOUR_CONNECTION_NAME" ipv4.dns "8.8.8.8 8.8.4.4"
$ sudo nmcli connection modify "YOUR_CONNECTION_NAME" ipv4.method manual

# 設定を反映するためにサービスをリスタート
$ sudo nmcli connection down "YOUR_CONNECTION_NAME"
$ sudo nmcli connection up "YOUR_CONNECTION_NAME"
```

### ssh設定

```bash
# boot直下にsshファイルを作成
$ sudo nano /boot/ssh

# sshサービスを起動し、自動起動設定を行う
$ sudo systemctl start ssh
$ sudo systemctl enable ssh

# confファイルでルートへのsshを禁止
$ sudo nano /etc/ssh/sshd_config
# PermitRootLogin noにする

# 再起動
$ sudo reboot now
```

### パッケージのアップデート

```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo apt autoremove
$ sudo apt clean
$ sudo reboot now
```

## その他

### USB起動の無効化

```bash
$ sudo rpi-eeprom-config --edit
```

```conf
# fと4を削除
BOOT_ORDER=0xf41

# 0x1
BOOT_ORDER=0x1
```

```bash
$ sudo reboot now
```