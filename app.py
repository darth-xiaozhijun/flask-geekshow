from flask import Flask, request, url_for, render_template
from models import User

app = Flask(__name__)


# GET 请求
@app.route("/")
def index():
    return "<h1>Hello World</h1>"


# POST 请求
@app.route("/user", methods=["POST"])
def hello_user():
    return "Hello User"


# 路径传参
@app.route("/user/<id>")
def user_id(id):
    return "hello user:" + id


# 问号传参
@app.route("/query/user")
def query_user():
    id = request.args.get("id")
    return "query user:" + id


# 反向路由
@app.route("/query_url")
def query_url():
    return "query url:" + url_for("query_user")


# 模板的使用
@app.route("/templates")
def template():
    content = "Hello templates"
    return render_template("index.html", content=content)


# 模板：对象传递
@app.route("/templates/user")
def template_user():
    user = User(1, "极客萧")
    return render_template("user_index.html", user=user)


# 模板：条件判断
@app.route("/templates/user/<user_id>")
def template_user_id(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, "极客萧")

    return render_template("user_id.html", user=user)


# 模板：循环
@app.route("/templates/user/list")
def template_user_list():
    users = []
    for i in range(10):
        user = User(i, "geekshow" + str(i))
        users.append(user)

    return render_template("user_list.html", users=users)


if __name__ == "__main__":
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()
