def welcome():
    print("请先登陆（admin 111111）")
    while 1:
        user=input("输入用户名")
        pwd=input("输入密码")
        if user=='admin' and pwd=='111111':
            print("成功")
            break
        else:
            print("输入错误 请再次重新输入")