# how many times each word appears in the txt file

fname = input('Enter the file name: ')  #e.g. www.py4inf.com/code/romeo.txt
try:
    fhand = open(fname)
except:
    print ('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print (counts)