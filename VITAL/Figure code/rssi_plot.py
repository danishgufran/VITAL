import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('i12p_engr0.csv')
df2 = pd.read_csv('pxl4_engr0.csv')

df1 = df1.drop(columns = ['x','y','label'])
df2 = df2.drop(columns = ['x','y','label'])

df1 = df1.head(10)
df2 = df2.head(10)

df1 = df1.iloc[: , 85:125]
df2 = df2.iloc[: , 85:125]

print(df1.shape)
print(df2.shape)

base = np.arange(start=0, stop=40, step=1)
print(base)
d1 = df1.to_numpy()[1]
d2 = df2.to_numpy()[1]
plt.plot( base.T, d1.T)
plt.plot( base.T, d2.T)
plt.legend(['i12p','pxl4'])
plt.show()