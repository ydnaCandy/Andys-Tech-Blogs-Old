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
# パーティション確認
lsblk -f
NAME        FSTYPE
sda
└─sda1      ntfs

# パーティション削除
sudo fdisk /dev/sda

Command (m for help): 


nで新しいパーティションを作成。
pで現在の状態を確認。
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
NAME FSTYPE
sda
└─sda1 ntfs

# フォーマット変更
sudo mkfs.ext4 /dev/sda1
mke2fs 1.46.2 (28-Feb-2021)
/dev/sda1 contains a ntfs file system
Proceed anyway? (y,N) y
/dev/sda1 is mounted; will not make a filesystem here!

# マウント解除
sudo umount /dev/sda1

udo mkfs.ext4 /dev/sda1
mke2fs 1.46.2 (28-Feb-2021)
/dev/sda1 contains a ntfs file system
Proceed anyway? (y,N) y

Creating journal (262144 blocks): 
done
Writing superblocks and filesystem accounting information: done 
```

```bash


```


```bash



sudo mkdir /mnt/my-ssd

# 
sudo mount -t ext4 /dev/sda1 /mnt/my-ssd

# マウント確認
df -h |grep ssd
/dev/sda1       234G   28K  222G   1% /mnt/my-ssd


sudo nano /etc/fstab

/dev/sda1 /mnt/my-ssd ext4 defaults 0 0

```
