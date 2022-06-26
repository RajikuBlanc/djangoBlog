from django.shortcuts import render
from django.http import HttpResponse

from app.forms import HelloForm
"""
! aaaaa
// aaaaaaaa
?    aaaa
TODO asasas
"""


# Create your views here.
def index(request):
    # http://127.0.0.1:8000/hello/?msg=hello
    # リクエストから値を取得
    # 以下の場合はパラメーターがない時はエラーになってしまう
    # msg = request.GET["msg"]

    # if文を使用してパラメーターがない時もエラーが吐かないようにする
    # パラメーターが存在したら
    # inはGET辞書の中に値が存在するかをチェックする
    # 値があればtrueなければfalseを返す
    # if "msg" in request.GET:
    # 	msg = request.GET["msg"]
    # 	result = "Hello World!" + msg
    # else:
    # 	result = "パラメーターを追加して"

    # javaとはキャスト方法が異なる
    # java → (String) id
    # python → str(id)
    # result = "あなたのID:" + str(id) + "あなたの名前:" + name
    # return HttpResponse(result)
    params = {"title": "Hello", "msg": "world", "goto": "next"}
    return render(request, "hello/index.html", params)


def next(request):
    params = {"title": "Hello", "msg": "Django", "goto": "index"}
    return render(request, "hello/index.html", params)


def form(request):
    msg = request.POST["msg"]
    params = {
        "title": "タイトル",
        "msg": "hello" + msg,
    }
    return render(request, "hello/index.html", params)


def formView(request):
    """
    共通の処理
    """
    params = {"title": "タイトル", "msg": "メッセージ", "form": HelloForm()}

    if request.method == "POST":
        params["msg"] = ("名前:" + request.POST["name"] + "</br>mail:" +
                         request.POST["mail"] + "</br>年齢:" +
                         request.POST["age"])
        params["form"] = HelloForm(request.POST)

    return render(request, "hello/index.html", params)
