import sys
droppedFile = sys.argv[1]
fo = open(droppedFile, "r")
lines = fo.readlines()
count = 0
sampleno=1
printing = False
internal = 0
temp=[]
datestore=""
timestore=""
output = open("output.txt", "w")
filename="Filename= "+droppedFile
title="Sample" +"    "  " CH4	      CO2	 N2O       Time	            Date"
print(filename,file=output)
print("\n",file=output)

print(title,file=output)
for line in lines:
    if "[Header]" in line:
        temp.append(str(timestore).ljust(15))
        temp.append(str(datestore).ljust(15))
        timestore=""
        datestore=""
        mySeparator = " "
        insert = mySeparator.join(temp)
        print(insert,file=output)
        print(temp)
        temp=[]
        printing = False
        gastype=0
        temp.append(str(sampleno).ljust(10))
        sampleno+=1
        
 
    if "[Peak Table(Ch1)]" in line:
        internal=0
        printing= True

    if "[Peak Table(Ch2)]" in line:
        internal=0
    
    if "[Peak Table(Ch3)]" in line:
        internal=0
        

    if printing :
        if internal == 1:
            if "0" in line:
                temp.append(str(0).ljust(10))
        
        if internal==3:
            date= line.split()
            insertval= date[4]
            temp.append(insertval.ljust(10))

        internal+=1

    if "Output Date" in line:
        date= line.split()
        datestore=date[2]
        
    
    if "Output Time" in line:
        timearr= line.split()
        timing= timearr[2]
        label= timearr[3]
        time= timing+label
        
        timestore=time


     
    count+=1    
    
temp.append(str(timestore).ljust(15))
temp.append(str(datestore).ljust(15))
insert = mySeparator.join(temp)
print(temp)
print(insert,file=output)
    
output.close()