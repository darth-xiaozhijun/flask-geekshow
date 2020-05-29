from flask import Flask, render_template, url_for, request, redirect
from wtforms import Form, TextField, PasswordField, validators

app = Flask(__name__)


class LoginForm(Form):
    username = TextField("username", [validators.Required()])
    password = PasswordField("password", [validators.Required()])


@app.route("/")
def index():
    return redirect(url_for("add"))


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        form = request.form
        adder1 = form.get("adder1")
        adder2 = form.get("adder2")
        message = int(adder1) + int(adder2)
        return render_template("add.html", adder1=adder1, adder2=adder2, message=message)
    return render_template("add.html")


@app.route("/user", methods=["POST","GET"])
def user():
    myForm = LoginForm(request.form)
    if myForm.username.data == "geekshow" and myForm.password.data == "123" and myForm.validate():
        return redirect("http://www.jikexueyuan.com")
    else:
        message = "Login Failed"
        return render_template("login2.html", message=message, form=myForm)
    return render_template("login2.html", form=myForm)


if __name__ == "__main__":
    app.run(port="8080")
