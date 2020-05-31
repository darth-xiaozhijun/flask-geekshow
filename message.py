from flask import Flask, render_template, url_for, request, redirect
from wtforms import Form, TextField, PasswordField, validators
from orm import Message

app = Flask(__name__)


class PublishForm(Form):
    message = TextField("message", [validators.Required()])
    sender = TextField("sender", [validators.Required()])


@app.route("/show", methods=['GET', 'POST'])
def show():
    myEntryForm = PublishForm(request.form)
    msgs = Message(None,None).selectAll()
    if request.method == 'POST':
        e = Message(myEntryForm.sender.data, myEntryForm.message.data)
        e.insertOne()
        return render_template("show.html", entries=msgs, form=myEntryForm)
    return render_template("show.html", entries=msgs, form=myEntryForm)


if __name__ == "__main__":
    app.run(port="8080")
