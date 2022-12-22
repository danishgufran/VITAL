import numpy as np
import matplotlib.pyplot as plt

p1 = [1,2,3]
e1 = [2.62,1.71,5.29]

p2 = [4,5,6]
e2 = [3.87,1.85,4.01]

p3 = [7,8,9]
e3 = [3.79,1.99,3.29]


import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.15
fig = plt.subplots(figsize =(7, 5))
 
# set height of bar
IT = [2.62, 2.66,1.71,3.29,7.5]
ECE = [3.87,3.7, 1.85,4.01,7.0]
CSE = [3.79,4.2,1.99,3.29, 7.9]
 
# Set position of bar on X axis
br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
# Make the plot
plt.bar(br1, IT, color ='r', width = barWidth,
        edgecolor ='grey', label ='Image Size - 206x206')
plt.bar(br2, ECE, color ='g', width = barWidth,
        edgecolor ='grey', label ='Image Size - 202x206')
plt.bar(br3, CSE, color ='b', width = barWidth,
        edgecolor ='grey', label ='Image Size - 210x206')
 
# Adding Xticks
plt.xlabel('Patch Size',fontsize=15)
plt.ylabel('Error in Meters',fontsize=15)
plt.xticks([r + barWidth for r in range(len(IT))],
        ['41x41','31x31', '20x20', '10x10', '5x5'],fontsize=15)
plt.yticks(np.arange(0, 8, step=0.5))
 
# plt.title("Sensitivity Analysis", fontweight ='bold', fontsize = 15)
plt.legend()
plt.show()
