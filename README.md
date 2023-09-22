# simple-chat-api-python

## 環境構築
コンテナの起動

初回のみ
```
cp project.env .env
```

imageのbuildとコンテナの立ち上げ
```
docker compose build
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

admin画面は`http://localhost:8008/api-admin/`で確認可能