# -*- coding: utf-8 -*-
import tabula
df = tabula.read_pdf("/Users/gangch/weiyun/16862794/我的文档/招行电子帐单/CreditCardReckoning201906.pdf",
                     encoding='utf-8',multiple_tables=True,pages='all')
#print(df)
df[1]