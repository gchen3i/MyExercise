# -*- coding: UTF-8 -*-
import tushare as ts
import pandas as pd
import pymysql
import pysnooper

pro = ts.pro_api('a0630d57359280860360068ff19e3073cdb73b5485eed124083a74fe')
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

@pysnooper.snoop()
def DragonTiger(date):
#指定日期的龙虎榜信息
    DT = pro.top_inst(trade_date=date)
    row = DT.shape[0]
# 定义要执行的sql语句
    cmd = 'insert into dragontiger_jg(No,ts_code,exalter,buy,buy_rate,sell,sell_rate,netbuy)' \
          'values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = DT[[1]]


    cursor.execute(cmd,val)

    last_id = cursor.lastrowid
    print("最后一条数据的ID是:", last_id)

# 涉及写操作要注意提交
    conn.commit()
DragonTiger('20190529')

# 关闭连接
cursor.close()
conn.close()