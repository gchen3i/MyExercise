#-*- coding: utf-8 -*-
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import  matplotlib.pyplot as plt

def sta001(k,nyear,xd):
    d2 = round(np.fv(k,nyear,-xd,-xd));
    return d2

d40 = 1.4*40
print("d40, 40 x 1.4=",d40)
d = sta001(0.05,40-1,1.4);
print("01 保守投资模式,",d,round(d/d40))
d2 = sta001(0.20,40-1,1.4);
print("02 激进投资模式,",d2,round(d2/d40))

dk = round(d2/d)
print("dk,两者差别(xx)倍",dk)

dx05 = [sta001(0.05,x,1.4) for x in range(0,40)]
dx10 = [sta001(0.10,x,1.4) for x in range(0,40)]
dx15 = [sta001(0.15,x,1.4) for x in range(0,40)]
dx20 = [sta001(0.20,x,1.4) for x in range(0,40)]

df = pd.DataFrame(columns=['dx05','dx10','dx15','dx20'])
df['dx05'] = dx05
df['dx10'] = dx10
df['dx15'] = dx15
df['dx20'] = dx20
print(" ")
print(df.tail())
df.plot()
plt.show()