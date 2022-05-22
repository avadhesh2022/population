import csv
import matplotlib.pylab as plt
data=[]
with open("population-estimates.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        data.append(row)
Brunei=Cambodia=Indonesia=Laos=Malaysia=Myanmar=Philippines=Singapore=Thailand=Vietnam=0 
for i in range(1,len(data)):
    if(data[i][0]=="Brunei Darussalam" and data[i][2]=="2014"):
        Brunei=float(data[i][3])
    if(data[i][0]=="Cambodia" and data[i][2]=="2014"):
        Cambodia=float(data[i][3])
    if(data[i][0]=="Indonesia" and data[i][2]=="2014"):
        Indonesia=float(data[i][3])
    if(data[i][0]=="Malaysia" and data[i][2]=="2014"):
        Malaysia=float(data[i][3])
    if(data[i][0]=="Myanmar" and data[i][2]=="2014"):
        Myanmar=float(data[i][3])
    if(data[i][0]=="Philippines" and data[i][2]=="2014"):
        Philippines=float(data[i][3])
    if(data[i][0]=="Singapore" and data[i][2]=="2014"):
        Singapore=float(data[i][3])
    if(data[i][0]=="Thailand" and data[i][2]=="2014"):
        Thailand=float(data[i][3])
    if(data[i][0]=="Viet Nam" and data[i][2]=="2014"):
        Vietnam=float(data[i][3])
    if(data[i][0]=="Lao People's Democratic Republic" and data[i][2]=="2014"):
        Laos=float(data[i][3])
country=[]
population=[]
population.extend([Indonesia,Thailand,Laos,Philippines,Singapore,Myanmar,Brunei,Malaysia,Vietnam,Cambodia])
country.extend(["Indonesia","Thailand","Loas","Philippines","Singapore","Myanmar","Brunei","Malaysia","Vietnam","Combodia"])
plt.bar(country,population)  
plt.xlabel("country name")
plt.ylabel("Population of asean country in the year 2014")
plt.legend()
plt.show()  
#Completed

