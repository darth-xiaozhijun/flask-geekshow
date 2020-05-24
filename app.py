from flask import Flask, request, url_for

app = Flask(__name__)


# GET 请求
@app.route("/")
def index():
    return "Hello World"


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


if __name__ == "__main__":
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()
