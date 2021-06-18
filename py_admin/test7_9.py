# 第七个功能
def test1():
    try:
        # 数据库导入配置
        import db
        db = db.db()
        cursor = db.cursor()
        query='''select stu.sno,sname,sc.grade
                from stu,sc
                where stu.sno=sc.sno and sc.grade<60'''
        cursor.execute(query)
        # print(query)
        while 1:
            res = cursor.fetchone()
            if res is None:
                break
            print(res)
        # result1 = cursor.fetchall()
        print(res)
    except IOError:
        print("err")

# 第八个功能
def test2():
    try:
        # 数据库导入配置
        import db
        db = db.db()
        cursor = db.cursor()
        str=input("输入课程名")
        query = '''select sname 学生姓名,stu.sno 学号 ,course.cno 课程号,grade 成绩 from 
                    stu,sc,course
                    where sc.sno = stu.sno 
                    and sc.cno=(select cno FROM
	                course where cname='%s')
                    and sc.cno=course.cno
                    '''%(str)
        cursor.execute(query)
        # print(query)
        while 1:
            res = cursor.fetchone()
            if res is None:
                break
            print(res)
        # result1 = cursor.fetchall()
        print(res)
    except IOError:
        print("err")

# 第9个功能
def test3():
    try:
        # 数据库导入配置
        import db
        db = db.db()
        cursor = db.cursor()
        index = input("请输入学生的姓")
        query = 'select sname from stu where sname like "{}%"'.format(index)
        # print(query)
        cursor.execute(query)
        # print(query)
        while 1:
            res = cursor.fetchone()
            if res is None:
                break
            print(res)
        # result1 = cursor.fetchall()
        print(res)
        db.close()
    except IOError:
        print("err")
