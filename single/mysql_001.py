import pymysql

conn = pymysql.connect(
    host='129.211.48.84',
    port=3306,
    user='gangch',
    password='@Spatial1',
    database='gangch',
    charset='utf8'
)
# 获取一个光标
cursor = conn.cursor()

# 定义要执行的sql语句

# sql = 'create table tutorials_tbl(' \
#       'tutorial_id INT NOT NULL AUTO_INCREMENT,' \
#       'tutorial_title VARCHAR(100) NOT NULL,' \
#       'tutorial_author VARCHAR(40) NOT NULL,' \
#       'submission_date DATE,' \
#       'PRIMARY KEY(tutorial_id))'
sql = 'insert into tutorials_tbl(tutorial_id,tutorial_title,tutorial_author) values (%s,%s,%s)'
val = ('2','test1','chengang')

# sql = 'insert into userinfo(user,pwd) values(%s,%s);'
# data = [
#     ('july', '147'),
#     ('june', '258'),
#     ('marin', '369')
# ]
# 拼接并执行sql语句
cursor.execute(sql,val)

last_id = cursor.lastrowid
print("最后一条数据的ID是:", last_id)

# 涉及写操作要注意提交
conn.commit()

# 关闭连接
cursor.close()
conn.close()

