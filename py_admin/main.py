import welcome
import test1
import test2
import test3
import test4
import test5
import test6
import test7_9
welcome.welcome()
while 1:
    print('''
    1.查询操作(单表查询、复杂查询)
    2.单表查询
    3.插入学生数据/选课信息
    4.更改学生专业信息/成绩信息
    5.查询特定学生的选课信息
    6.查询特定学院/专业的所有学生
    7.查询小于60分的所有学生
    8.查询选修了某门课的所有学生的信息及成绩
    9.查询某姓的所有学生
    '''
    )
    choose=input("输入要选择的功能")
    if choose == '1':
        test1.test1()
    elif choose == '2':
        test2.test1()
    elif choose == '3':
        test3.test1()
    elif choose=='4':
        test4.test1()
    elif choose == '5':
        test5.test1()
    elif choose == '6':
        test6.test1()
    elif choose == '7':
        test7_9.test1()
    elif choose == '8':
        test7_9.test2()
    elif choose == '9':
        test7_9.test3()
    a = input("输入0退出，其他键继续")
    if a == '0':
        break
print("跳出循环了")


