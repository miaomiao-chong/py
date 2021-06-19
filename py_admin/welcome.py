import db
db = db.db()
cursor = db.cursor()
def welcome():
    print("请先登陆（目前仅限管理员账户登录，学生账户暂不支持）")
    while 1:
        id=input("输入用户名")
        pwd=input("输入密码")
        sql = 'SELECT * FROM adminuser'
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        for index in range (len(results)):
            print(results[index])
welcome()