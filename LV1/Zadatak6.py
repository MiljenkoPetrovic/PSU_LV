import re
email = re.compile('\w+@\w+\.[a-z]{3}')

mailovi=[]
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
            print(domain)

        
#print(mailovi)



    
