import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


mtcars = pd.read_csv('mtcars.csv') 
print("------------------------------------------------------------------------------------------------------------------------------------------")
print(mtcars.sort_values(by='mpg').head(5))
print("------------------------------------------------------------------------------------------------------------------------------------------")
mt=mtcars[(mtcars.cyl==8)]
print(mt.sort_values(by='mpg',ascending=False).head(3))
print("------------------------------------------------------------------------------------------------------------------------------------------")
mt6=mtcars[(mtcars.cyl==6)]
print("Srednja vrijednost je: ",mt6["mpg"].mean())
print("------------------------------------------------------------------------------------------------------------------------------------------")
mt4=mtcars[(mtcars.cyl==4) & (mtcars.wt > 2) & (mtcars.wt < 2.2)]
print("Srednja vrijednost mpg-a automobila sa 4 cilindra i masom između 2000 i 2200 lb je: ",mt4["mpg"].mean())
print("------------------------------------------------------------------------------------------------------------------------------------------")
mtauto=mtcars[(mtcars.am==0)]
mtruc=mtcars[(mtcars.am==1)]
print("Ima: ",len(mtauto), "automobila sa automatskim mjenjacem")
print("Ima: ",len(mtruc), "automobila sa rucnim mjenjacem")
print("------------------------------------------------------------------------------------------------------------------------------------------")
print("Ima: ",len(mtauto[mtauto.hp>100]), "automobila sa automatskim mjenjacem i hp > 100")
print("------------------------------------------------------------------------------------------------------------------------------------------")
mtkg=mtcars.wt*1000*0.45
mtcars.wt=mtkg
print(mtcars)
