def test1():
    try:
        # 数据库导入配置
        import db
        db = db.db()
        cursor = db.cursor()
        a=eval(input("输入1更改学生专业信息，2更改成绩信息："))
        if a==1 :
            sno=input("输入要修改学生的学号")
            mno=input("输入专业号")
            sql = "update stu set mno=%s where sno=%s"%(mno,sno)
            # sql = "update stu set mno=102 where sno=1001"
        elif a==2:
            sno = input("输入学号")
            cno = input("输入课程号")
            grade=input("输入成绩")
            sql = "update sc set grade=%s where sno=%s and cno=%s" % (grade, sno,cno)
            # sql = "update stu set mno=102 where sno=1001"
        print(sql)
        cursor.execute(sql)
        db.commit()
        # print(query)
        while 1:
            print("成功")
            res = cursor.fetchone()
            if res is None:
                break
            print(res)
        # result1 = cursor.fetchall()
        print(res)
        db.close()
    except IOError:
        print("err")