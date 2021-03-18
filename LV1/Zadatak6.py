import re
email = re.compile('\w+@\w+\.[a-z]{3}')
dictionary={}
mailovi=[]
i=0
string="From:" 
try:
    fhand = open("LV1\mbox-short.txt")
except:
    print ('File cannot be opened:', fhand)
    exit()

i=0
for line in fhand:
    line = line.rstrip()
    if line.startswith(string) and "From:" in line:
            mailovi.extend(email.findall(line))
            domain = line.split('@')[1]
            if domain not in dictionary:
                dictionary[domain]=1
            elif domain in dictionary:
                dictionary[domain]+=1
        

res=[]
for i in mailovi: 
    if i not in res: 
        res.append(i) 




for i in range(5):
    print(res[i])
    

for x, y in dictionary.items():
    print(x, ":", y)




    
