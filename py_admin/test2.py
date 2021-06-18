def test1():
    try:
        # 数据库导入配置
        import db
        db=db.db()
        # print('连接成功')
        cursor = db.cursor()
        # detail=-1
        # sql_1 = "SHOW databases"
        # sql_1 =  "would it be the %s when we meet in %s"%(detail)   格式化字符串：用%s
        # print(sql_1)
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