from flask import Blueprint
from orm import User

user = Blueprint('user', __name__)


@user.route('/<int:userid>')
def showUser(username, password):
    uu = User(username, password)
    u = User.selectOne(uu)
    return u
