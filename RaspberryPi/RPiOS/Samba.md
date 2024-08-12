# 外部ストレージをマウント

## 実施環境

```bash
cat /etc/os-release
>>> PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
>>> NAME="Debian GNU/Linux"
>>> VERSION_ID="11"
>>> VERSION="11 (bullseye)"
>>> VERSION_CODENAME=bullseye
>>> ID=debian
>>> HOME_URL="https://www.debian.org/"
>>> SUPPORT_URL="https://www.debian.org/support"
>>> BUG_REPORT_URL="https://bugs.debian.org/"
```

## 手順

```bash
sudo apt install samba

df -h |grep ssd

mkdir /home/admin/shared

sudo nano /etc/samba/smb.conf


```

```conf
[shared]
   path = /mnt/my-ssd
   browseable = yes
   writeable = yes
   create mask = 0777
   directory mask = 0777
   public = no
```