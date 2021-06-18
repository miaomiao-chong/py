def test1():
    try:
        # 数据库导入配置
        import db
        db = db.db()
        cursor = db.cursor()
        index = eval(input("请输入需要插入表的序号：1(学生表) 2(选课表) 要注意每输入一个数据都需要回车"))
        if index == 1:
            # sno=eval(input())
            # sname=input()
            # ssex=input()
            # sbirth=input()
            # birthplace=input()
            # nation=input()
            # sclass=eval(input())
            # mno=eval(input())
            # cursor.execute(query)
            # print(query)
            # 方便起见直接造数据了
            print("方便起见直接造数据了")
            data = (2001,"haha","男","2020.0.0","山东菏泽","汉",101,101)
            query='insert into stu values(%d,"%s","%s","%s","%s","%s",%d,%d)'%(data)
            print(query)
            cursor.execute(query)
        elif index== 2:
            sno = input("输入学号：")
            cno=input("输入课程号")
            grade=input("输入成绩")
            sql = "insert into sc values(%s,%s,%s)"%(sno,cno,grade)
            # query = 'insert into sc values(1052,500002,85)'
            cursor.execute(sql)
        db.commit()
        while 1:
            res = cursor.fetchone()
            if res is None:
                break
            print(res)
        # result1 = cursor.fetchall()
        print(res)
        print("添加成功")
        db.close()
    except:
        print("err")