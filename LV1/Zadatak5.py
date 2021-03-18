
#Program radi samo kad unesem putanju
import re
string="X-DSPAM-Confidence:"
fp = input('Enter the file path: ')  
try:
    fhand = open(fp)
except:
    print ('File cannot be opened:', fhand)
    exit()

suma=0
count=0
for line in fhand:
    line = line.rstrip()
    if line.startswith(string):
            br = re.findall("\d+\.\d+", line)
            res = list(map(float, br)) 
            suma+=sum(res)
            count=count+1


print("Srednja vrijednost: ",suma/count)
