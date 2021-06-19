# 用户表的创建及删除以及增删改信息操作
import db
db = db.db()
cursor = db.cursor()
# choose = eval(input("输入1新建管理员表，输入2新建学生表:"))
def createUserTable(choose):
    # 1:管理员  2:学生
    if choose==1:
        table='adminUser'
    if choose==2:
        table='stuUser'
    str1="""create table %s(
       id int(11) NOT NULL AUTO_INCREMENT,
       name varchar(20),
       password varchar(20),
        PRIMARY KEY (id) 
    )"""%(table)
    cursor.execute(str1)
    # print("执行成功")
    while 1:
        print("执行成功")
        res = cursor.fetchone()
        if res is None:
            break
        print(res)
    db.close()
# createUserTable(choose)

def dropUserTable(choose):
    if choose == 1:
        table = 'adminUser'
    if choose == 2:
        table = 'stuUser'
    str1 = """drop table if exists %s""" % (table)
    cursor.execute(str1)
    print("表删除成功")
# dropUserTable(1)

def insertUser(choose):
    if choose == 1:
        table = 'adminUser'
    if choose == 2:
        table = 'stuUser'
    id=eval(input("输入id"))
    password=input("输入密码")
    str1='''insert into %s values (%s,"%s")'''%(table,id,password)
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
        table = 'stuUser'
    id=eval(input("输入id："))
    pwd = input("输入修改后的密码：")
    str1='''update %s set password='%s' where id=%s
    '''%(table,pwd,id)
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
# updateUser(1)

def deleteUser(choose):
    if choose == 1:
        table = 'adminUser'
    if choose == 2:
        table = 'stuUser'
    id=eval(input("输入id："))
    str1='''delete from %s where id=%s
    # '''%(table,id)
    print(str1)
    cursor.execute(str1)
    db.commit()
    print("执行成功")
deleteUser(1)