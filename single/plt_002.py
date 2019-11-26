import os
import pandas as pd
path = r'/Users/gangch/Downloads/'
df = pd.read_csv(path+'iris.data',names=['sepal length','sepal width','petal length','petal width','class'])

import matplotlib.pyplot as plt
plt.style.use('ggplot')
#%matplotlib inline
import numpy as np
fig , ax = plt.subplots(figsize=(6,4))
ax.hist(df['petal width'],color='black')
ax.set_ylabel('Count',fontsize=12)
ax.set_xlabel('Width',fontsize=12)
plt.title('Iris Petal Width',fontsize=14,y =1.01)