from flask import Flask, render_template, url_for, request, redirect
from wtforms import Form, TextField, PasswordField, validators
from orm import User

app = Flask(__name__)


class LoginForm(Form):
    username = TextField("username", [validators.Required()])
    password = PasswordField("password", [validators.Required()])


@app.route("/user", methods=["POST", "GET"])
def user():
    myForm = LoginForm(request.form)
    if request.method == "POST":
        user = User(myForm.username.data, myForm.password.data)
        if user.isExist():
            return redirect("http://www.jikexueyuan.com")
        else:
            message = "Login Failed"
            return render_template("login2.html", message=message, form=myForm)
    return render_template("login2.html", form=myForm)


@app.route("/register", methods=["POST", "GET"])
def register():
    myForm = LoginForm(request.form)
    if request.method == "POST":
        user = User(myForm.username.data, myForm.password.data)
        user.insertOne()
        return "Register Success"
    return render_template("login2.html", form=myForm)


if __name__ == "__main__":
    app.run(port="8080")
