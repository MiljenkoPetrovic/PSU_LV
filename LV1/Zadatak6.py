fhand = open('mbox-short.txt') # www.py4inf.com/code/mbox-short.txt
for line in fhand:
line = line.rstrip()
if line.startswith('From:'):
print line