from flask import Flask, request, url_for, render_template, flash, abort
from models import User

app = Flask(__name__)
app.secret_key = "123"


# GET 请求
@app.route("/hello")
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


# 模板：继承
@app.route("/templates/base/one")
def template_base_one():
    return render_template(("base_one.html"))


@app.route("/templates/base/two")
def template_base_two():
    return render_template(("base_two.html"))


# 消息提示
@app.route("/msg")
def hello_world():
    flash("hello geekshow")
    return render_template("msg.html")


# 用户登录
@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')

    if not username:
        flash("please input username")
        return render_template("login.html")
    if not password:
        flash("please input password")
        return render_template("login.html")

    if username == 'geekshow' and password == '123456':
        flash("login success")
        return render_template("login.html")
    else:
        flash("username or password is wrong")
        return render_template("login.html")


# 返回前端页面
@app.route("/login")
def login_html():
    return render_template("login.html")


# 错误页面
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route('/users/<user_id>')
def users(user_id):
    if int(user_id) == 1:
        return render_template("user.html")
    else:
        abort(404)


if __name__ == "__main__":
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()
