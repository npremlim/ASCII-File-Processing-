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
co2= False
output = open("output.txt", "w")
filename="Filename= "+droppedFile
title="Sample" +"    "  " CH4	      CO2	 N2O       Time	            Date"
import pandas as pd
df = pd.DataFrame(columns=['CH4', 'CO2', 'N2O', 'Time','Date'])

print(filename,file=output)
# print("\n",file=output)

# print(title,file=output)
co2peak=0
start=False
for line in lines:
    if "[Header]" in line and start:
            temp.append(str(timestore).ljust(15))
            temp.append(str(datestore).ljust(15))
            timestore=""
            datestore=""
            mySeparator = " "
            insert = mySeparator.join(temp)
            # print(len(temp))
            
            df.loc[len(df)] = temp
            # print(insert,file=output)
            # print(temp,file=output)
            #print(temp)
            temp=[]
            printing = False
            gastype=0
            # temp.append(str(sampleno).ljust(10))
            sampleno+=1
        
 
    if "[Peak Table(Ch1)]" in line:
        co2= False
        internal=0
        printing= True

    if "[Peak Table(Ch2)]" in line:
        internal=0
        co2= True
    
    if "[Peak Table(Ch3)]" in line:
        co2= False
        internal=0
        

    if printing :
       
        if internal == 1:
            peaks= line.split()
            peakno = int(peaks[3])
            if co2:
                co2peak= int(peaks[3])
            if "0" in line:
                temp.append(str(0).ljust(10))

           
        
        if internal>=3 and peakno!=0:
            date= line.split()
            insertval= date[4]
            if(co2):
                if(float(date[1])<7.70 or float(date[1])>7.90):
                    insertval="0"
                    #print("co2 val is "+ date[1])
                    
            if co2:
                if(co2peak==1):
                    temp.append(insertval.ljust(10))
                co2peak-=1
            else:
                temp.append(insertval.ljust(10))
            peakno-=1

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
    start=True   


# temp.append(str(timestore).ljust(15))
# temp.append(str(datestore).ljust(15))
temp.append(str(timestore).ljust(15))
temp.append(str(datestore).ljust(15))
# insert = mySeparator.join(temp)
df.loc[len(df)] = temp
# print(temp)
# print(insert,file=output)
# print(temp,file=output)
print(df.to_csv(), file=output)

output.close()