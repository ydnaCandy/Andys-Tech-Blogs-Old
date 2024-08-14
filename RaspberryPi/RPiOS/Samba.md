# 外部ストレージをマウントしてSambaで共有フォルダを作成する

## 実施環境

```bash
cat /etc/os-release
>>> PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
>>> NAME="Debian GNU/Linux"
>>> VERSION_ID="12"
>>> VERSION="12 (bookworm)"
>>> VERSION_CODENAME=bookworm
>>> ID=debian
>>> HOME_URL="https://www.debian.org/"
>>> SUPPORT_URL="https://www.debian.org/support"
>>> BUG_REPORT_URL="https://bugs.debian.org/"
```

## 外部ストレージのマウント手順

```bash
# パーティション確認
$ lsblk -f
>>> NAME        FSTYPE
>>> sda
>>> └─sda1      ntfs

# パーティション削除
$ sudo fdisk /dev/sda

Command (m for help): 

Command (m for help): d # dでパーティション削除
>>> Selected partition 1
>>> Partition 1 has been deleted.

Command (m for help): p 
Disk /dev/sda: 238.47 GiB, 256060514304 bytes, 500118192 sectors

Command (m for help): n # nで新規パーティションを作成
>>> Partition type
>>>    p   primary (0 primary, 0 extended, 4 free)
>>>    e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1): # Enter
First sector (65535-500118191, default 65535): # Enter
Last sector, +/-sectors or +/-size{K,M,G,T,P} (65535-500118191, default 500118191): # Enter
>>> Created a new partition 1 of type 'Linux' and of size 238.4 GiB.

Command (m for help): p
>>> Disk /dev/sda: 238.47 GiB, 256060514304 bytes, 500118192 sectors

Command (m for help): w
>>> The partition table has been altered.
>>> Syncing disks.

# フォーマット確認
lsblk -f
>>> NAME FSTYPE
>>> sda
>>> └─sda1 ntfs

# フォーマット変更
$ sudo mkfs.ext4 /dev/sda1
>>> mke2fs 1.46.2 (28-Feb-2021)
>>> /dev/sda1 contains a ntfs file system
>>> Proceed anyway? (y,N) y
>>> /dev/sda1 is mounted; will not make a filesystem here!

# マウント解除
$ sudo umount /dev/sda1
```


```bash
# マウント用のディレクトリ作成
$ sudo mkdir /mnt/my-ssd

# マウント
$ sudo mount -t ext4 /dev/sda1 /mnt/my-ssd

# マウント確認
$ df -h |grep ssd
>>> /dev/sda1       234G   28K  222G   1% /mnt/my-ssd

# 起動時に自動でマウントするように設定する
$ sudo nano /etc/fstab
```

```conf
# 末尾に追加
/dev/sda1 /mnt/my-ssd ext4 defaults 0 0
```




## Sambaの設定手順

```bash
# Sambaのインストール
sudo apt install samba samba-common-bin -y
sudo apt install samba-vfs-modules

# マウントを確認
df -h |grep ssd

# confファイルを開く
sudo nano /etc/samba/smb.conf
```

```conf
# iOSからも画像を保存できるようにするための設定
[global]
# iOS
fruit:nfs_aces = no
fruit:aapl = yes
vfs objects = catia fruit streams_xattr

# 共有するフォルダの設定
[my-ssd]
   path = /mnt/my-ssd
   browseable = yes
   writeable = yes
   create mask = 0777
   directory mask = 0777
   public = no
```

```bash
# sambaユーザーの設定
$ sudo smbpasswd -a [user]
>>> # ここで設定したパスワードが別端末からのアクセス時に使用される

# sambaサービスの再起動
sudo systemctl restart smbd
sudo systemctl restart nmbd

```

```bash
# 他端末からファイルを保存できるようにディレクトリの権限を変更する
$ chmod 777 /mnt/my-ssd
```
