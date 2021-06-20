import search
import  insert
import handleUserTable
import  update
import  delete
def adminUser():
    while 1:
        print('''
          1.查询操作(单表查询、打印全表、复杂查询)
          2.建立新表/删除新表(管理员用户/普通用户表)
          3.插入学生数据/选课信息/管理员用户/普通用户
          4.更改学生专业信息/成绩信息/用户密码
          5.删除学生相关信息/管理员用户/普通用户
                      '''
                  )
        choose=input("输入要选择的功能")

        if choose == '1':
            print("                  查询操作子界面")
            print("           ========================")
            print('''
                1.单表查询
                2.查询特定学生的选课信息
                3.查询特定学院/专业的所有学生
                4.查询小于60分的所有学生
                5.查询选修了某门课的所有学生的信息及成绩
                6.查询某姓的所有学生
                7.打印全表
                ''')
            a=eval(input())
            search.search(a)
        elif choose == '2':
            print("        建表/删表子界面（管理员用户表与普通用户表）")
            print("          ========================")
            print('''
                       1.建表
                       2.删表
                       ''')
            a = eval(input())
            if a==1:
                adminOrPutong=eval(input("新建哪个表？ 1：管理员 2:普通用户"))
                handleUserTable.createUserTable(adminOrPutong)
            if a==2:
                adminOrPutong = eval(input("删除哪个表？ 1：管理员 2:普通用户"))
                handleUserTable.dropUserTable(adminOrPutong)
        elif choose == '3':
            print("           插入操作子界面")
            print("       ========================")
            print('''
              1.增加学生数据
              2.增加选课信息
              3.增加管理员用户
              4.增加普通用户
                  ''')
            a = eval(input())
            insert.insert(a)
        elif choose=='4':
            print("           更改操作子界面")
            print("       ========================")
            print('''
             1.更改学生专业信息
             2.更改学生成绩信息
             3.更改管理员用户密码
             4.更改普通用户密码
                         ''')
            a = eval(input())
            update.update(a)
        elif choose == '5':
            print("            删除操作子界面")
            print("       ========================")
            print('''
         1.删除学生信息
         2.删除管理员用户
         3.删除普通用户
                                ''')
            a = eval(input())
            delete.delete(a)
        choose=-1   # 实现子功能的循环执行
        a = input("输入0退出，其他键继续")
        if a == '0':
            break
    print("跳出循环了")

