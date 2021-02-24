import csv
import math

import numpy as n
import random as r

numbers = [n.random.normal(100,20,500),
           n.random.normal(40,10,500),
           n.random.normal(150,50,500),
           n.random.normal(90,5,500)]

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        numbers[i][j] = round(numbers[i][j],1)

numbers = n.transpose(numbers)
for i in range(r.randint(0,100)):
    numbers[r.randint(1,499)][r.randint(1,3)] = n.nan

with open("test.csv", "w" , newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Заголовок 1","Заголовок 2","Заголовок 3","Заголовок 4"])
    writer.writerows(numbers)

def MaxInList():
    max = numbers[0][0]
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if numbers[i][j] > max:
                max = numbers[i][j]
    return max

def MinInList():
    min = numbers[0][0]
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if numbers[i][j] < min:
                min = numbers[i][j]
    return min

def AverageinList():
    count = 0
    sum = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if math.isnan(numbers[i][j]) != True :
                sum += numbers[i][j]
                count += 1
    return sum/count

print(MaxInList(),MinInList(),AverageinList())
print(n.nanmax(numbers),n.nanmin(numbers))