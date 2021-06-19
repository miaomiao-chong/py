import db
import  handleUserTable
db = db.db()
cursor = db.cursor()
def updateStuMajor():
    sno=input("输入要修改学生的学号")
    mno=input("输入专业号")
    sql = "update stu set mno=%s where sno=%s"%(mno,sno)
    # sql = "update stu set mno=102 where sno=1001"
    cursor.execute(sql)
    db.commit()
def updateStuGrade():
    sno = input("输入学号")
    cno = input("输入课程号")
    grade=input("输入成绩")
    sql = "update sc set grade=%s where sno=%s and cno=%s" % (grade, sno,cno)
    cursor.execute(sql)
    db.commit()
def update(a):
    if a==1:
        updateStuMajor()
    if a==2:
        updateStuGrade()
    if a==3:
        handleUserTable.updateUser(1)
    if a == 4:
        handleUserTable.updateUser(2)

