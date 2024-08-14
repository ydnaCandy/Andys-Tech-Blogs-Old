# Docker初期セットアップ手順

## 設定環境
- ハードウェア
    - Raspberry Pi 4
- OS
    - Raspberry Pi OS bookworm


## 手順

```bash
# 依存関係があるパッケージを一度削除
$ for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

# インストール
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc


# Add the repository to Apt sources:
$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

$ sudo apt update
```

```bash
# インストール
$ sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 起動確認
$ sudo docker run hello-world

# dockerコマンドで権限がないエラーが出る
$ docker ps -a
>>> permission denied while trying to connect to the Docker daemon socket a

# dockerのグループを確認
$ grep docker /etc/group
>>> docker:x:984:

# グループにユーザーを追加
$ sudo usermod -aG docker [user]

# 確認
$ grep docker /etc/group
>>> docker:x:984:goku

# 再起動して設定を反映
$ sudo reboot now

# dockerコマンドが通ることを確認
```



## 参考
- https://docs.docker.com/engine/install/debian/
