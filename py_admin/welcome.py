import db
db = db.db()
cursor = db.cursor()
def welcome():
    print("请先登陆（目前仅限管理员账户登录，学生账户暂不支持）")
    while 1:
        username=input("输入用户名")
        pwd=input("输入密码")
        sql = 'SELECT * FROM adminuser where username=%s'%(username)
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        if(len(results)!=0):
            if pwd==results[0][1]:
                print("登录成功")
                break
            else:
                print("输入错误")
        else:
            print("输入错误")
welcome()