# # sql_1 = "select  from stu where sno="
# # print(sql_1)
# # detail = input("输入学生学号")
# # sql_1 = sql_1 +  detail
# # print(sql_1)
#
# # 字符串拼接
# # a =333
# # b=444
# # str_word3 = 'hello, word! {} {}'
# # str_word3.format(a,b)
# # print(str_word3)
#
# # table = 'daa'
# # name = 45
# # sex = '''aaa'''
# # mixStr = str(name) + sex
# # string = 'insert into {} values ({}'.format(table, mixStr) + ')'
# # print(string)
#
#
# from pymysql import *
#
#
#
#   # 创建connection连接
#
#
#   # 执行sql语句   不行啊
#   # query = 'insert into 表名(列名1, 列名2, 列名3, 列名4, 列名5, 列名6) values(%s, %s, %s, %s, %s, %s)'
#   # 列名1 = 值1
#   # 列名2 = 值2
#   # 列名3 = 值3
#   # 列名4 = 值4
#   # 列名5 = 值5
#   # 列名6 = 值6
#   # values = (列名1, 列名2, 列名3, 列名4, 列名5, 列名6)
#   # cs1.execute(query, values)
#   #
#   # # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
#   # conn.commit()
#   #
#   # # 关闭cursor对象
#   # cs1.close()
#   # # 关闭connection对象
#   # conn.close()
#
# # con.execute(‘insert into USER表 values("%s", "%s","%s", "%s")‘  % \ (first_name,last_name,age,sex,income))
# # str = 'insert into %s values ("%s", "%s","%s", "%s")'%('aaa','bbb','ccc','ddd','eee')
# #
# print(str)
#
# a=input()
# b=input()
# str ='insert into aaa values ("%s", "%s","%s", "%s")'%(a,b,a,b)
# print(str)
# # a, b, c = map(int, raw_input('请输入3个整数, 用空格分隔：').split())   # 如果是Python 3, 自行替换raw_input为input print '\n输入3个整数为：%s %s %s'%(a, b, c)
# index = input("请输入学生的姓")
# query = 'select sname from stu where sname like "{}%"'.format(index)
# print(query)
#
# a=input()
# b=input()
# print(a,b)

# sno=input()
# sname=input()
# ssex=input()
# sbirth=input()
# birthplace=input()
# nation=input()
# sclass=input()
# mno=input()
# query='insert into stu values("%s","%s","%s","%s","%s","%s","%s","%s")'%(sno,sname,ssex,sbirth,birthplace,nation,sclass,mno)
# print(query)



import search
search.search1()
search.search2()