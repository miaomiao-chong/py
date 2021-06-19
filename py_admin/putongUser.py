import search
def putong():
    while 1:
         print("              普通用户只有查询功能")
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

         a = input("输入0退出，其他键继续")
         if a == '0':
            break
    print("跳出循环了")