import csv
import math
import numpy as n
import random as r
import pandas as p

numbers = [n.random.normal(100, 20, 500),
           n.random.normal(40, 10, 500),
           n.random.ranf(500),
           n.random.gumbel(200, 100, 500)]

numbers = n.transpose(numbers)

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        numbers[i][j] = round(numbers[i][j], 1)

for i in range(r.randint(0, 20)):
    numbers[r.randint(1, 499)][r.randint(0, 3)] = n.nan
    numbers[r.randint(1, 499)][r.randint(0, 3)] = 100000

df = p.DataFrame(numbers,columns=["длинна", "ширина", "вес", "объем"])
df.to_csv("data.csv", index=False, encoding= 'utf-8')

with open("test.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["длинна", "ширина", "вес", "объем"])
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
            if math.isnan(numbers[i][j]) != True:
                sum += numbers[i][j]
                count += 1
    return sum / count


print(MaxInList(), MinInList(), AverageinList())
print(n.nanmax(numbers), n.nanmin(numbers))