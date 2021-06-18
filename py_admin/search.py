import db
db = db.db()
cursor = db.cursor()
#
def quanbiao():
    try:
        sql_1 ="select  * from stu where sno="
        sql_2 = "select * from sc"
        sql_3 = "select * from major where mno="
        sql_4 = "select * from academy where yno= "
        sql_5 = "select * from course where cno = "
        a=eval(input("请输入要查询哪一个表 1(学生表),2(成绩表),3(专业表),4(学院表),5(选修课程表)"))
        if a==1:
            detail = input("输入学生学号")
            sql_1 = sql_1 + detail
            print(sql_1)
            print("  学号  姓名      1性别     出生日期    籍贯    民族    年级    专业号")
            cursor.execute(sql_1)
        elif a==2:
            sno=input("输入学号")
            cno=input("输入专业号")
            sql_2=sql_2+' where sno='+sno + ' and cno = '+cno
            print(" 学号  专业号  分数")
            # print(sql_2)
            cursor.execute(sql_2)
        elif a== 3:
            mno=input("输入专业号")
            sql_3=sql_3+ mno
            print(sql_3)
            print(" 专业号    专业名   专业类别   所在学院")
            cursor.execute(sql_3)
        elif a == 4:
            yno=input("输入学院号")
            print(" 学院号  学院名  院长")
            sql_4=sql_4+yno
            print(sql_4)
            cursor.execute(sql_4)
        elif a == 5:
            cno=input("请输入课程号")
            sql_5=sql_5+cno
            print("课程号    专业名 学分 所属学院")
            cursor.execute(sql_5)
        else: print("请输入数字1-5")
        while 1:
            res = cursor.fetchone()
            if res is None:
                break
            print(res)
        # result1 = cursor.fetchall()
        print(res)

    except Exception as e:
        print(e)
    db.close()
# 第五个功能
def search1():
    try:
        a=input("输入学生的名字")
        sql = '''
            select cname 选修课名 ,grade 成绩 from course,sc
            where course.cno=sc.cno and sc.sno=(
	        select sno from stu 
	        where sname="%s")
        '''%(a)
        # print(sql)
        cursor.execute(sql)
        # print(query)
    except IOError:
        print("err")
# 第六个功能
def search2():
    try:
        # 数据库导入配置
        import db
        db = db.db()
        cursor = db.cursor()
        count=0
        a=eval(input("请输入1(查询特定学院)、2查询特定专业"))
        if a==1:
            str=input("输入学院名")
            sql='''
            select sname 学生姓名
            from stu,major,academy
            where stu.mno=major.mno AND 
            major.yno=academy.yno and
            major.yno =(SELECT yno from
		        academy where yname='%s'
            )'''%(str)

        if a==2:
            str=input("请输入专业名")
            sql='''
            select sname 学生名,mname 专业名
            from stu,major
            where stu.mno=major.mno and major.mname='%s' '''%(str)
        # print(sql)
        cursor.execute(sql)
        while 1:
            # print("成功")
            count=count+1
            res = cursor.fetchone()
            if res is None:
                break
            print(res)
        # result1 = cursor.fetchall()
        print(res)
        # print("总人数",str(count))
        db.close()
    except IOError:
        print("err")

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
