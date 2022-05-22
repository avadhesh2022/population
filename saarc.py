import csv
import matplotlib.pylab as plt
from matplotlib.pyplot import xlabel
data=[]
with open("population-estimates.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        data.append(row)
pakistan=srilanka=nepal=india=bangladesh=bhutan=maldiv=afganistan={}
for i in range(1,len(data)):
    if(data[i][0]=="Pakistan"):
        a=data[i][2]
        b=data[i][3]
        pakistan[a]=b
        
    if(data[i][0]=="Maldives"):
        a=data[i][2]
        b=data[i][3]
        maldiv[a]=b
        
    if(data[i][0]=="Nepal"):
        a=data[i][2]
        b=data[i][3]
        nepal[a]=b
        
    if(data[i][0]=="Sri Lanka"):
        a=data[i][2]
        b=data[i][3]
        srilanka[a]=b
        
    if(data[i][0]=="Bhutan"):
        a=data[i][2]
        b=data[i][3]
        bhutan[a]=b
        
    if(data[i][0]=="India"):
        a=data[i][2]
        b=data[i][3]
        
        india[a]=b
    if(data[i][0]=="Afghanistan"):
        a=data[i][2]
        b=data[i][3]
        afganistan[a]=b
    if(data[i][0]=="Bangladesh"):
        a=data[i][2]
        b=data[i][3]
        bangladesh[a]=b
p=[0 for i in range(1950,2016)]
year=[i for i in range(1950,2016)]
j=0 
for i in india.values():
    p[j]+=float(i)
    j+=1
j=0 
for i in pakistan.values():
    p[j]+=float(i)
    j+=1
j=0 
for i in nepal.values():
    p[j]+=float(i)
    j+=1
j=0 
for i in bhutan.values():
    p[j]+=float(i)
    j+=1
j=0 
for i in srilanka.values():
    p[j]+=float(i)
    j+=1
j=0 
for i in bangladesh.values():
    p[j]+=float(i)
    j+=1
j=0 
for i in maldiv.values():
    p[j]+=float(i)
    j+=1
j=0 
for i in afganistan.values():
    p[j]+=float(i)
    j+=1
plt.barh(year,p)  
plt.xlabel("population of saarc countries")
plt.ylabel("year")
plt.show() 

