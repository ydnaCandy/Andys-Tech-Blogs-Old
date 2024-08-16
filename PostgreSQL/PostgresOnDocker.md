# Dockerを使ってPostgreSQLを構築

## 環境

- ハードウェア
    - Raspberry Pi 4
- OS
    - Raspberry Pi OS bookworm

## Docker Composeを使った構築手順

```bash
# homeから実行
$ mkdir docker/postgres

$ nano compose.yml
```


```yml
services:
  db:
    image: postgres:15
    container_name: postgres-db
    environment:
      POSTGRES_USER: [user] # postgres
      POSTGRES_PASSWORD: [password] # postgres
      POSTGRES_DB: sampledb
    ports:
      - "15432:5432"
    volumes:
      - /var/appdata/postgres:/var/lib/postgresql/data
```

## バックアップとリストアのコマンド

```bash
# バックアップ
$ docker exec -t postgres-db pg_dump -U postgres -d sampledb -F c -f /var/lib/postgresql/data/mydb.dump

# リストア
$ docker exec -i postgres-db pg_restore -U user -d mydb -1 /var/lib/postgresql/data/mydb.dump
```

### 検証

```yml
# ベースとなるPostgresコンテナを起動
services:
  db:
    image: postgres:15
    container_name: pg-base
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: basedb
    ports:
      - "15432:5432"
    volumes:
      - /var/appdata/postgres_base:/var/lib/postgresql/data
```

```bash
# psqlに入る
$ docker exec -it pg-base psql -U postgres -d basedb

# テーブル作成
basedb=# CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) 
);
>>> CREATE TABLE

# テーブルの確認
basedb=# \d
                List of relations
 Schema |       Name       |   Type   |  Owner   
--------+------------------+----------+----------
 public | employees        | table    | postgres
 public | employees_id_seq | sequence | postgres
(2 rows)

# ダンプファイルの生成
docker exec -t pg-base pg_dump -U postgres -d basedb -F c -f /var/lib/postgresql/data/mydb.dump
```


```yml
# リストア先のPostgresコンテナ
services:
  db:
    image: postgres:15
    container_name: pg-copy
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: copydb
    ports:
      - "25432:5432"
    volumes:
      - /var/appdata/postgres_copy:/var/lib/postgresql/data

```

```bash
# リストア先のコンテナを起動
cd cp_pg
docker compose up -d

# ダンプしたファイルをコピー
sudo cp /var/appdata/postgres_base/mydb.dump /var/appdata/postgres_copy/mydb.dump

# リストア
docker exec -i pg-copy pg_restore -U postgres -d copydb -1 /var/lib/postgresql/data/mydb.dump

# リストアの確認
$ docker exec -it pg-copy psql -U postgres -d copydb

copydb=# \d
>>> List of relations
>>>  Schema |       Name       |   Type   |  Owner   
>>> --------+------------------+----------+----------
>>>  public | employees        | table    | postgres # テーブルが生成されている
>>>  public | employees_id_seq | sequence | postgres
>>> (2 rows)
```