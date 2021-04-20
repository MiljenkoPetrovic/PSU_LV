import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv') 
mt=mtcars[(mtcars.cyl==8)]
mt6=mtcars[(mtcars.cyl==6)]
mt4=mtcars[(mtcars.cyl==4)]
fig = plt.figure()
mtcars.bar(cyl,mpg)
plt.show()