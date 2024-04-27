# simple-chat-api-python

## 環境構築
コンテナの起動

初回のみ
```
cp project.env .env
```

コンテナの立ち上げ
```
docker compose up -d
```

コンテナの中にアクセス
```
docker compose exec django_app bash
```

## サーバー起動
初期データを登録
```shell
develop_tools/clean_up_db.sh
develop_tools/load_fixtures.sh
```

サーバー起動
```shell
python manage.py runserver
```
