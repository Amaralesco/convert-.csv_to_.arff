import pandas as pd 


#Little Scrip that converts .csv files to .arff
#Takes out the " from the file and swaps ; for ,
#Also makes the #N/A from excell to ?

#File that we are going to create
#My location:
#D:\Program Files\Python\Ficheiros\data
#Your's might be different change next line accordingly
fout = open('data/student-port(com+classes).txt', 'x') #creates the file

#File that we are going to open
#Location:
#D:\Program Files\Python\Ficheiros\data
#Your's might be different change next line accordingly
f = open('data/student-port(com+classes).csv')
       
for line in f:
    line = line.rstrip("\n")
    line = line.replace("\"","")
    #line = line.replace(",0",".")
    line = line.replace(",",".")
    line = line.replace(";",",")
    line = line.replace("#N/A","?")
    fout.write(line + "\n")
    

else:
    
    print("")
                
     
            
     
   