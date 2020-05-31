# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/python')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


class User(Base):
    # 表的名字:
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def insertOne(self):
        try:
            # 创建session对象:
            session = DBSession()
            session.add(self)
            session.commit()
            return self.id
        except Exception as e:
            session.rollback()
            return e
        finally:
            session.close()

    def selectOne(self):
        # 创建session对象:
        session = DBSession()
        users = session.query(User).filter(User.username == self.username, User.password == self.password).first()
        session.close()
        return users

    def isExist(self):
        # 创建session对象:
        session = DBSession()
        users = session.query(User).filter(User.username == self.username, User.password == self.password).first()
        session.close()
        return 0 if users is None else 1


class Message(Base):
    # 表的名字:
    __tablename__ = 't_message'
    id = Column(Integer, primary_key=True)
    sender = Column(String(255), unique=True)
    message = Column(String(255), unique=True)

    def __init__(self, sender, message):
        self.sender = sender
        self.message = message

    def insertOne(self):
        try:
            # 创建session对象:
            session = DBSession()
            session.add(self)
            session.commit()
            return self.id
        except Exception as e:
            session.rollback()
            return e
        finally:
            session.close()

    def selectAll(self):
        # 创建session对象:
        session = DBSession()
        messages = session.query(Message).all()
        session.close()
        return messages


if __name__ == "__main__":
    # user = User("111111", "1234")
    # user.add()
    user = User("111111", "1234")
    result = user.selectOne();
    print(result.username)
    print(user.isExist())
    print(Message(None,None).selectAll())
