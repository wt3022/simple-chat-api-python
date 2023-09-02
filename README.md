# simple-chat-api-python

## 環境構築
```
cp project.env .env
docker compose up -d
```

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

admin画面は`http://localhost:8008/api-admin`で確認可能