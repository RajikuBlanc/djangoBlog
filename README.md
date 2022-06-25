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

## views.pyとurls.pyを修正
- urls.pyはcontrollerの役割
  - パスによって呼び出す関数を指定したり、名前をつけることができる
  - 基本的には各アプリに追加で作成する
  - <>を使用して引数を受け取ってviewsに渡せる
  - 整数を使用する場合はintを指定しなければならない
     ```python
	urlpatterns = [
		path("<int:id>/<name>/", views.index, name="index"),
	]
	```
- views.pyはserviceの役割
  - 関数を定義して処理を行う
  - 戻り値はテンプレート名かHttpResponseが基本

## tempaltesディレクトリの作成
- テンプレートの格納先はtemplatesという名前でないといけない
- urlのパスと同じ階層に置く
	- パスが'localhost/hello'の場合
	- templates/hello/htmlファイルじゃないといけない

## viewsから値を受け取る
  - views.py
  ```python
  def index(request):
    params = {"title": "Hello", "msg": "Django"}
    return render(request, "hello/index.html", params)
  ```
  render関数の第3引数に渡したい値を設定する

  - index.html
  - 変数は{{}}で囲むことで取得できる
  ```html
    <p>{{title}}</p>
    <p>{{msg}}</p>
  ```

  ## 画面遷移
  - views.py
  ```python
  def index(request):
    params = {"title": "Hello", "msg": "World", "goto": "next"}
    return render(request, "hello/index.html", params)

  def next(request):
    params = {"title": "Hello", "msg": "Django", "goto": "index"}
  	return render(request, "hello/index.html", params)
  ```

  - urls.py
  ```python
  urlpatterns = [
    path("", views.index, name="index"),
    path("next/", views.next, name="next"),
  ]
  ```
  - index.html
  - urlテンプレートタグにはurls.pyのname属性を指定する
  ```html
    <p>{{title}}</p>
    <p>{{msg}}</p>
    <a href="{% url goto %}">{{goto}}</a>
  ```
