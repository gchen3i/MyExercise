import tushare as ts
import pandas as pd
from sqlalchemy import create_engine
import time
pro = ts.pro_api('a0630d57359280860360068ff19e3073cdb73b5485eed124083a74fe')

dates =pro.trade_cal(exchange='', start_date='20190103', end_date='20190523')
x = dates['cal_date'].loc[dates['is_open'].isin(['1'])]
for date in x:
    print(date)
    data =pro.daily(trade_date=date)
    print(data)
    print(date)
    myconn = create_engine('mysql+pymysql://gangch:@Spatial1@129.211.48.84:3306/gangch?charset=utf8')
    pd.io.sql.to_sql(data,'stock_kd', myconn, schema='gangch', if_exists='append')
    time.sleep(30)