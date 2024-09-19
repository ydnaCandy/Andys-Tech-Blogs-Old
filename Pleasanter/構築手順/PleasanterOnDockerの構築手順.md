# PleasanterをDockerを使って構築する手順

## 参考
- https://hub.docker.com/r/implem/pleasanter

## 環境
- ハードウェア
    - Raspberry Pi 4
- OS
    - Ubuntu 24.04 Desktop


## 手順

1. dockerを立ち上げるディレクトリを作成する

    ```bash
    $ cd pleasanter
    ```

2. ディレクトリの中に`.env`ファイルを作成する
    - ユーザー名やパスワードはすべて`postgres`にしています。

    ```env
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=postgres
    POSTGRES_HOST_AUTH_METHOD=scram-sha-256
    POSTGRES_INITDB_ARGS="--auth-host=scram-sha-256"
    Implem_Pleasanter_Rds_PostgreSQL_SaConnectionString='Server=db;Database=postgres;UID=postgres;PWD=postgres'
    Implem_Pleasanter_Rds_PostgreSQL_OwnerConnectionString='Server=db;Database=#ServiceName#;UID=#ServiceName#_Owner;PWD=postgres'
    Implem_Pleasanter_Rds_PostgreSQL_UserConnectionString='Server=db;Database=#ServiceName#;UID=#ServiceName#_User;PWD=postgres'
    ```

3. compose.ymlを作成する

    ```yml
    services:
      db:
        container_name: postgres
        image: postgres:15
        ports:
          - "15432:5432"
        environment:
          - POSTGRES_USER
          - POSTGRES_PASSWORD
          - POSTGRES_DB
          - POSTGRES_HOST_AUTH_METHOD
          - POSTGRES_INITDB_ARGS
        restart: always
        volumes:
          - /var/dockervol/psql/data:/var/lib/postgresql/data
        networks:
          pleasanter_net:
            ipv4_address: 172.99.0.2

      pleasanter:
        container_name: pleasanter
        image: implem/pleasanter
        depends_on:
          - db
        ports:
          - "13500:8080"
        environment:
          Implem.Pleasanter_Rds_PostgreSQL_SaConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_SaConnectionString}
          Implem.Pleasanter_Rds_PostgreSQL_OwnerConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_OwnerConnectionString}
          Implem.Pleasanter_Rds_PostgreSQL_UserConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_UserConnectionString}
        restart: always
        networks:
          pleasanter_net:
            ipv4_address: 172.99.0.3

      codedefiner:
        container_name: codedefiner
        image: implem/pleasanter:codedefiner
        depends_on:
          - db
        environment:
          Implem.Pleasanter_Rds_PostgreSQL_SaConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_SaConnectionString}
          Implem.Pleasanter_Rds_PostgreSQL_OwnerConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_OwnerConnectionString}
          Implem.Pleasanter_Rds_PostgreSQL_UserConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_UserConnectionString}
        networks:
          pleasanter_net:
            ipv4_address: 172.99.0.4


    networks:
      pleasanter_net:
        driver: bridge
        ipam:
          driver: default
          config:
            - subnet: 172.99.0.0/24

    ```

4. codedifnerを実行

    ```bash
    $ docker compose run codedefiner _rds 
    ```

5. Pleasanterを起動

    ```bash
    $ docker compose up -d pleasanter
    ```

6. ブラウザからPleasanterにアクセスして起動していること





## DBとPleasanterを別端末で構築する

まずはpostgresを起動する

.envファイルを作成

```conf
# .envで保存
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_HOST_AUTH_METHOD=scram-sha-256
POSTGRES_INITDB_ARGS="--auth-host=scram-sha-256"

# Server部分にサーバー側のIPを指定
Implem_Pleasanter_Rds_PostgreSQL_SaConnectionString='Server=192.168.3.100:15432;Database=postgres;UID=postgres;PWD=postgres'
Implem_Pleasanter_Rds_PostgreSQL_OwnerConnectionString='Server=192.168.3.100:15432;Database=#ServiceName#;UID=#ServiceName#_Owner;PWD=postgres'
Implem_Pleasanter_Rds_PostgreSQL_UserConnectionString='Server=192.168.3.100:15432;Database=#ServiceName#;UID=#ServiceName#_User;PWD=postgres'
```


```yml
# postgresのみ起動
services:
  db:
    container_name: postgres
    image: postgres:15
    ports:
      - "15432:5432"
    environment:
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB
      - POSTGRES_HOST_AUTH_METHOD
      - POSTGRES_INITDB_ARGS
```

```yml
# pleasanter側
services:
  pleasanter:
    container_name: pleasanter
    image: implem/pleasanter
    ports:
      - "13500:8080"
    environment:
      Implem.Pleasanter_Rds_PostgreSQL_SaConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_SaConnectionString}
      Implem.Pleasanter_Rds_PostgreSQL_OwnerConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_OwnerConnectionString}
      Implem.Pleasanter_Rds_PostgreSQL_UserConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_UserConnectionString}

  codedefiner:
    container_name: codedefiner
    image: implem/pleasanter:codedefiner
    environment:
      Implem.Pleasanter_Rds_PostgreSQL_SaConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_SaConnectionString}
      Implem.Pleasanter_Rds_PostgreSQL_OwnerConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_OwnerConnectionString}
      Implem.Pleasanter_Rds_PostgreSQL_UserConnectionString: ${Implem_Pleasanter_Rds_PostgreSQL_UserConnectionString}

```