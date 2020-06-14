import pymysql

conn = pymysql.connect("localhost", "root", "123456", "python")

# 创建游标
cursor = conn.cursor()

# 安装模块
# python -m pip install -i https://mirrors.aliyun.com/pypi/simple/ pymysql

def insert(username, password):
    insert_sql = "insert into T_USER(username,password) values ('{0}','{1}')".format(username, password)
    cursor.execute(insert_sql)
    conn.commit();


def select(username, password):
    sql = "select * from T_USER where username = '{0}' and password = '{1}'".format(username, password)
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) == 0:
        return False
    else:
        return True

def test():
    username1 = input("请输入用户名：")
    password1 = input("请输入密码：")

    # 插入数据
    # insert_sql = "insert into T_USER(id) values (7)"
    insert_sql = "insert into T_USER(username,password) values ('{0}','{1}')".format(username1, password1)
    print(insert_sql)
    cursor.execute(insert_sql)
    conn.commit();

    # 查询数据
    sql = "select * from T_USER"
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row)
