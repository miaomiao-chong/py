import db
db = db.db()
cursor = db.cursor()
def welcome():
    a=eval(input("请先登陆：输入1 管理员用户登录，输入2 普通用户登录:"))
    if a==1:
        table='adminUser'
    if a==2:
        table='putongUser'
    while 1:
        username=input("输入用户名")
        pwd=input("输入密码")
        sql = 'SELECT * FROM %s where username=%s'%(table,username)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        if(len(results)!=0):
            if pwd==results[0][1]:
                print("登录成功")
                return a
            else:
                print("输入错误")
        else:
            print("输入错误")
            continue
        continue
        return a
# welcome()
