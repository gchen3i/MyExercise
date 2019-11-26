# -*- coding: UTF-8 -*-
import tushare as ts
import pandas as pd

data_dir ='/Users/gangch/python/data'
pro = ts.pro_api('a0630d57359280860360068ff19e3073cdb73b5485eed124083a74fe')

def PriceDaily(code,s_date,e_date):
#指定日期范围的日行情
    data = pro.daily(ts_code=code,startdate=s_date,end_date=e_date)
    data.to_csv('%s/%s_日线%s-%s.csv' %(data_dir,code,s_date,e_date),encoding='utf_8_sig')

def DrangonTiger(date):
#指定日期的龙虎榜信息
    DT = pro.top_inst(trade_date=date)
    print(DT)
    DT.to_csv('%s/龙虎榜机构_%s.csv' %(data_dir,date), encoding='utf_8_sig', mode='w', header=True)

    df = pro.top_list(trade_date=date)
    print(df)
    df.to_csv('%s/龙虎榜每日_%s.csv' %(data_dir,date),encoding='utf_8_sig')

def TopTenFloatHold(code,s_date,e_date):
    data = pro.top10_floatholders(ts_code='code', start_date=s_date, end_date=e_date)
    #data.to_csv('%s/%s_流通股%s-%s.csv' % (data_dir, code, s_date, e_date), encoding='utf_8_sig')
    data.to_csv('%s/流通股%s-%s.csv' % (data_dir, code, s_date, e_date), encoding='utf_8_sig')

#=====================================================================================================

# PriceDaily('002559.sz','20170101','20190514')
#
# Trade_date = pro.trade_cal(exchange=' ', start_date='20190515', end_date='20190517')
#
# for date in Trade_date['cal_date'].loc[Trade_date['is_open'].isin(['1'])] :
#     提取所有开市的日期
#     DrangonTiger(date)
DrangonTiger('20190516')

# TopTenFloatHold('002151.sz','20180101','20190331')
# all_stock = pd.read_csv('%s/all_stock.csv' %data_dir,skiprows=1,sep=',',encoding='utf_8_sig')
#for single in all_stock['ts_code']:
#数据源有次数限制
 #   TopTenFloatHold(single,'20180101','20190331')