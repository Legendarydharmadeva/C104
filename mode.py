import csv
from collections import Counter
from operator import mod

with open('data.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

data = Counter(new_data)
modedataforrange = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height, occurence in data.items():
    if 50<float(height)<60 :
        modedataforrange["50-60"]+= occurence
    elif 60<float(height)<70:
        modedataforrange["60-70"]+= occurence
    elif 70<float(height)<80:
        modedataforrange["70-80"]+= occurence
mode_range,mode_occcurence = 0,0
for range,occurence in modedataforrange.items() :
    if occurence>mode_occcurence:
        mode_range,mode_occcurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((mode_range[0]+mode_range[1])/2)

print(mode)