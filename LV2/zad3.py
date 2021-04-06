import numpy as np
from matplotlib import pyplot
from matplotlib import pyplot as plt
import os


os.chdir("LV2")

filename="mtcars.csv"



try:
    data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

except:
    print ('File cannot be opened:', filename)
    exit()

pyplot.scatter(data[:,0],data[:,3],c='b',s=data[:,5]*15)

arr=[]

Minimum=min(data[:,0])
Maximum=max(data[:,0])
Suma=sum(data[:,0])/len(data[:,0])


for i,item in enumerate(data[:,1]):
    if item >=6:
        arr.append(data[i,0])

   
print(Minimum)
print(Maximum)
print(Suma)


plt.show()