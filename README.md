# Django Blog Project

## 仮想環境の作成
- fishでvenvを起動する場合は.fishファイルを使用する
```fish
source myvenv/bin/activate.fish
```

## パッケージのインストール
```fish
pip3 install -r requirements.txt
```

## Djangoプロジェクトの作成
```fish
django-admin startproject config .
```

## データベースのセットアップ
```fish
python3 manage.py migrate
```

## Webサーバーの起動
```fish
python3 manage.py runserver
```

## アプリケーションの作成
```fish
python3 manage.py startapp app
```

## 管理ユーザーの作成
```fish
python3 manage.py createsuperuser
```

## models.pyを編集
- モデルを追加する
```python
def __str__(self):
		return self.title
```

## 管理画面追加
modelのクラス名をregisterの引数に与えることで管理画面で管理できる
```python
admin.site.register(Post)
```

## データベース構築
- models.pyを修正した場合はデータベースの構築をしなければならない
```fish
python3 manage.py makemigrations
python3 manage.py migrate
```
