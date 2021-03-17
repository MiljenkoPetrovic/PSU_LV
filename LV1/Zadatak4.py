count=0
unos=0
zbroj=0
max_num = -2147483647
min_num =  2147483648
while unos != 'Done':
    
    unos=input("Unosite brojeve te kad ste gotovi unesite done\n")
    try: 
        broj = int(unos)
    
        count=count+1
        zbroj=zbroj+broj
        if broj > max_num:
            max_num = broj
        
        if broj < min_num:
            min_num = broj
    except ValueError:
        if unos != 'Done':
            print("Ne valja unos")
    
print("unjeli ste ", count, " broja")  
print("Najmanji broj je ",min_num)
print("Najveci broj je ",max_num)
print("Zbroj je ",zbroj)
print("Srednja vrijednost je ", zbroj/count)

