import csv
import matplotlib.pylab as plt
import numpy as np
data=[]
with open("population-estimates.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        data.append(row)
Brunei={}
Cambodia={}
Indonesia={}
Laos={}
Malaysia={}
Myanmar={}
Philippines={}
Singapore={}
Thailand={}
Vietnam={}
for i in range(1,len(data)):
    if(data[i][0]=="Brunei Darussalam" and int(data[i][2])>=2004 and int(data[i][2])<=2014):
        a=int(data[i][2])
        b=float(data[i][3])
        Brunei[a]=b
    if(data[i][0]=="Cambodia" and int(data[i][2])>=2004 and int(data[i][2])<=2014):
        a=int(data[i][2])
        b=float(data[i][3])
        Cambodia[a]=b
    if(data[i][0]=="Indonesia" and int(data[i][2])>=2004 and int(data[i][2])<=2014):
        a=int(data[i][2])
        b=float(data[i][3])
        Indonesia[a]=b
    if(data[i][0]=="Malaysia" and int(data[i][2])>=2004 and int(data[i][2])<=2014):
        a=int(data[i][2])
        b=float(data[i][3])
        Malaysia[a]=b
    if(data[i][0]=="Myanmar" and int(data[i][2])>=2004 and int(data[i][2])<=2014):
        a=int(data[i][2])
        b=float(data[i][3])
        Myanmar[a]=b
    if(data[i][0]=="Philippines" and int(data[i][2])>=2004 and int(data[i][2])<=2014):
        a=int(data[i][2])
        b=float(data[i][3])
        Philippines[a]=b
    if(data[i][0]=="Singapore" and int(data[i][2])>=2004 and int(data[i][2])<=2014):
        a=int(data[i][2])
        b=float(data[i][3])
        Singapore[a]=b
    if(data[i][0]=="Thailand" and int(data[i][2])>=2004 and int(data[i][2])<=2014):
        a=int(data[i][2])
        b=float(data[i][3])
        Thailand[a]=b
    if(data[i][0]=="Viet Nam" and int(data[i][2])>=2004 and int(data[i][2])<=2014):
        a=int(data[i][2])
        b=float(data[i][3])
        Vietnam[a]=b
    if(data[i][0]=="Lao People's Democratic Republic" and int(data[i][2])>=2004 and int(data[i][2])<=2014):
        a=int(data[i][2])
        b=float(data[i][3])
        Laos[a]=b
lebels=[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
brunei=[]
cambodia=[]
indonesia=[]
laos=[]
malaysia=[]
myanmar=[]
philippines=[]
singapore=[]
thailand=[]
vietnam=[]
for i in range(2004,2015):
    brunei.append(Brunei[i])
    cambodia.append(Cambodia[i])
    indonesia.append(Indonesia[i])
    laos.append(Laos[i])
    malaysia.append(Malaysia[i])
    myanmar.append(Myanmar[i])
    philippines.append(Philippines[i])
    singapore.append(Singapore[i])
    thailand.append(Thailand[i])
    vietnam.append(Vietnam[i])

x=np.arange(11)
width=0.05
plt.bar(x-0.2, brunei, width, color='cyan')
plt.bar(x-0.15,cambodia, width, color='orange')
plt.bar(x-0.1, indonesia, width, color='green')
plt.bar(x-0.05, laos, width, color='gold')
plt.bar(x, malaysia, width, color='red')
plt.bar(x+0.05, myanmar, width, color='brown')
plt.bar(x+0.1, philippines, width, color='tomato')
plt.bar(x+0.15, singapore, width, color='plum')
plt.bar(x+0.2, thailand, width, color='orange')
plt.bar(x+0.25, vietnam, width, color='navy')
plt.xticks(x, [2004, 2005, 2006, 2007, 2008,2009,2010,2011,2012,2013,2014])
plt.xlabel("Years")
plt.ylabel("Population")
plt.legend([ "Brunei", "Cambodiya", "Indonesia","Laos", "Malaysia", "Myanmar","Philippines", "Singapore", "Thailand", "Vietnam"])
plt.show()
##Completed

