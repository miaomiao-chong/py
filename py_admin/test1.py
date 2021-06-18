def test1():
    # 数据库导入配置
    import db
    # 连接数据库的函数
    db=db.db()
    # print('连接成功')
    cursor = db.cursor()
    # sql_1 = "SHOW databases"
    sql_1 = "select * from stu"
    sql_2 = "select * from sc"
    sql_3 = "select * from major"
    sql_4 = "select * from academy"
    sql_5 = "select * from course"
    a=input("请输入要查询哪一个表 1(学生表),2(成绩表),3(专业表),4(学院表),5(选修课程表)")
    # a='4'
    if a=='1':
        print("  学号  姓名      1性别     出生日期    籍贯    民族    年级    专业号")
        cursor.execute(sql_1)
    elif a=='2':
        print(" 学号  专业号  分数")
        cursor.execute(sql_2)
    elif a== '3':
        print(" 专业号    专业名   专业类别   所在学院")
        cursor.execute(sql_3)

    elif a == '4':
        print(" 学院号  学院名  院长")
        cursor.execute(sql_4)
    elif a == '5':
        print("课程号    专业名 学分 所属学院")
        cursor.execute(sql_5)

    while 1:
        res = cursor.fetchone()
        if res is None:
            break
        print(res)
    # result1 = cursor.fetchall()
    print(res)
    db.close()