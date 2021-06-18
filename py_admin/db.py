import pymysql
def db():
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='111111',
        db='students',
        charset='utf8'
    )
    # print(111)
    return db
