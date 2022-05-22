import csv
import matplotlib.pylab as plt
from matplotlib.pyplot import xlabel
data=[]
with open("population-estimates.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        data.append(row)
year=[]
popu=[]
for i in range(len(data)):
    if(data[i][0]=='India'):
        year.append(int(data[i][2]))
        popu.append(data[i][3])

plt.legend()
plt.bar(year,popu)
plt.grid()
plt.xlabel("year")
plt.ylabel("India's population")

plt.show()
#Completed

    