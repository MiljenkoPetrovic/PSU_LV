fname = input('Enter the file name: ')  
try:
    fread = fopen.readlines(fname, mode='r+')
except:
    print ('File cannot be opened:', fname)
    exit()




line='X-DSPAM-Confidence:'
 for line in fread:
    
      if x in line:

          print(line)