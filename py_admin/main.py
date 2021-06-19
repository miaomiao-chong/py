import welcome
import search
import test1
import test2
import test3
import test4
import test6
import test7_9
# welcome.welcome()
choose='-1'   # 实现子功能的循环执行
while 1:
    if choose=='-1':    # 子功能不循环执行
        print('''
                       1.查询操作(单表查询、复杂查询)
                       2.建立新表/删除新表(管理员用户/学生用户表)
                       2.插入学生数据/选课信息/管理员用户/学生用户
                       3.更改学生专业信息/成绩信息
                       4.删除学生相关信息/学生用户/管理用户
                       '''
              )
        choose=input("输入要选择的功能")

    if choose == '1':
        print("                  查询操作子界面")
        print("           ========================")
        print('''
            1.全表查询
            2.查询特定学生的选课信息
            3.查询特定学院/专业的所有学生
            4.查询小于60分的所有学生
            5.查询选修了某门课的所有学生的信息及成绩
            6.查询某姓的所有学生
            ''')
        a=eval(input())
        b=search.search(a)
        if b!=0:
            continue
    elif choose == '2':
        test2.test1()
    elif choose == '3':
        test3.test1()
    elif choose=='4':
        test4.test1()
    elif choose == '5':
        # test5.test1()
        print("aaa")
    elif choose == '6':
        test6.test1()
    elif choose == '7':
        test7_9.test1()
    elif choose == '8':
        test7_9.test2()
    elif choose == '9':
        test7_9.test3()
    choose=-1   # 实现子功能的循环执行
    a = input("输入0退出，其他键继续")
    if a == '0':
        break
print("跳出循环了")


