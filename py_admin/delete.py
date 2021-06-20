import db
import  handleUserTable
db = db.db()
cursor = db.cursor()
def deleteStu():
    sno=input("输入要删除学生的学号")
    sql = '''delete from stu where sno  = %s''' %(sno)
    cursor.execute(sql)
    db.commit()
    print("删除成功")
def delete(a):
    if a==1:
        deleteStu()
    if a==2:
        handleUserTable.deleteUser(1)
    if a==3:
        handleUserTable.deleteUser(2)

