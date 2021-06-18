def test1():
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
