import handleUserTable
import db
db = db.db()
cursor = db.cursor()
def insertstu():
    print("方便起见直接造数据了")
    data = (2001,"haha","男","2020.0.0","山东菏泽","汉",101,101)
    query='insert into stu values(%d,"%s","%s","%s","%s","%s",%d,%d)'%(data)
    print(query)
    cursor.execute(query)
    db.commit()
    print("执行成功")
def insertCourse():
    sno = input("输入学号：")
    cno=input("输入课程号")
    grade=input("输入成绩")
    sql = "insert into sc values(%s,%s,%s)"%(sno,cno,grade)
    # query = 'insert into sc values(1052,500002,85)'
    cursor.execute(sql)
    db.commit()
    print("执行成功")
def insert(a):
    if a == 1:
        insertstu()
    if a == 2:
        insertCourse()
    elif a==3:
        handleUserTable.insertUser(1)
    elif a == 4:
        handleUserTable.insertUser(2)

    isquit=eval(input("要继续执行查询操作吗 输0退出"))
    return isquit