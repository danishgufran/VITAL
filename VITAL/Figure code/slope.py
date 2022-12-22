import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

base = ['VITAL', 'CNNLoc', 'ANVIL', 'SHERPA', 'WiDeep']
data = [[1.18,2.98,1.2,1.31,3.47],[1.8,2.55,1.9,2,4.47]]
df = pd.DataFrame(data, columns = base)

colors = ['#769465', '#69BDE0', '#E06D5E', '#2F7694', '#94E069']
fig, ax = plt.subplots(1, figsize=(10,5), facecolor='darkgrey')
ax.set_facecolor('darkgrey')
for i, v in enumerate(base):
    # get a single country from the list
    temp = df[v]
    # plot the lines
    plt.plot(temp[0], temp[1], 
             color=colors[i], lw=2.5, 
             marker='o', markersize=5)
    
# x limits, x ticks, and y label 
# plt.xlim(2017.5,2019.5)
# plt.xticks([2018, 2019])
plt.ylabel('USD')
# get y ticks, replace 1,000 with k, and draw the ticks
yticks = plt.yticks()

# grid
ax.xaxis.grid(color='black', linestyle='solid', which='both', alpha=0.9)
ax.yaxis.grid(color='black', linestyle='dashed', which='both', alpha=0.1)
# remove spines
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.title('GDP Per Capta\n', loc='left', fontsize=20)
plt.show()