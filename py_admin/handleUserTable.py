# 用户表的创建及删除以及增删改信息操作
import db
db = db.db()
cursor = db.cursor()
# choose = eval(input("输入1新建管理员表，输入2新建学生表:"))
def createUserTable(choose):
    # 1:管理员用户  2:普通用户
    if choose==1:
        table='adminUser'
    if choose==2:
        table='putongUser'
    str1="""create table %s(
       username varchar(20) not null,
       password varchar(20),
       phonenum varchar(20),
        PRIMARY KEY (username,password)
    )"""%(table)
    print(str1)
    cursor.execute(str1)
    # print("执行成功")
    while 1:
        print("执行成功")
        res = cursor.fetchone()
        if res is None:
            break
        print(res)
    db.close()
# createUserTable(1)
def dropUserTable(choose):
    if choose == 1:
        table = 'adminUser'
    if choose == 2:
        table = 'putongUser'
    str1 = """drop table if exists %s""" % (table)
    cursor.execute(str1)
    print("表删除成功")
# dropUserTable(1)
def insertUser(choose):
    if choose == 1:
        table = 'adminUser'
    if choose == 2:
        table = 'putongUser'
    username=input("输入用户名")
    password=input("输入密码")
    phonenum=input("输入电话号")
    str1='''insert into %s values ("%s","%s","%s")'''%(table,username,password,phonenum)
    cursor.execute(str1)
    db.commit()
    print("执行成功")
    while 1:
        res = cursor.fetchone()
        if res is None:
            break
        print(res)
    # result1 = cursor.fetchall()
    print(res)
    # print(str1)
# insertUser(1)
def updateUser(choose):
    if choose == 1:
        table = 'adminUser'
    if choose == 2:
        table = 'putongUser'
    username=input("输入username：")
    pwd = input("输入修改后的密码：")
    str1='''update %s set password='%s' where username=%s
    '''%(table,pwd,username)
    cursor.execute(str1)
    db.commit()
    print("执行成功")
    # print(str1)
# updateUser(1)
def deleteUser(choose):
    if choose == 1:
        table = 'adminUser'
    if choose == 2:
        table = 'putongUser'
    username=input("输入username：")
    str1='''delete from %s where username=%s
    # '''%(table,username)
    print(str1)
    cursor.execute(str1)
    db.commit()
    print("执行成功")
# deleteUser(1)

# dropUserTable(1)
# createUserTable(1)
# insertUser(1)
# updateUser(1)
# deleteUser(1)