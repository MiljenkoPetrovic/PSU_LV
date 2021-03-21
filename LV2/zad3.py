import re
import numpy as np
import matplotlib.pyplot as plt
import os
filename="LV2\mtcars_info.txt"
os.change.dir(LV2)




try:
    data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

except:
    print ('File cannot be opened:', filename)
    exit()

matplotlib.pyplot.scatter