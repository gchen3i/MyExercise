# -*- coding: UTF-8 -*-
import tushare as ts
data_dir ='/Users/gangch/python/data'
pro = ts.pro_api('a0630d57359280860360068ff19e3073cdb73b5485eed124083a74fe')

df = pro.trade_cal(exchange='', start_date='20190501', end_date='20190601', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
# 显示非交易日期
print(df)

data = pro.stock_basic(exchange='',list_status='L',fields='ts_code,symbol,name,area,industry,list_date')
# 显示股票列表
print(data)
data.to_csv('%s/all_stock.csv' %data_dir,encoding='utf_8_sig')

TopTen = pro.hsgt_top10(trade_date='20190513',market_type='1')
#成交量前十股票
print(TopTen)

Daily_600825 = pro.daily(ts_code='600825.sh',start_date='20160101',end_date='20190514')
#日线行情
Daily_600825.to_csv('%s/600825.csv' %data_dir,encoding='utf_8_sig')

Drangon_Tiger = pro.top_inst(trade_date='20190513')
Drangon_Tiger.to_csv('%s/龙虎榜.csv' %data_dir,encoding='utf_8_sig',mode='a',header=False)
