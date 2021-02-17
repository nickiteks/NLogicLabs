import csv
import numpy as n
import random as r

#numbers = n.random.normal(500,15,(500,4))
numbers = [[r.randint(40,50) for i in range(500)],
           [r.randint(500,520) for i in range(500)],
           [r.randint(400,440) for i in range(500)],
           [r.randint(20,25) for i in range(500)]]

numbers = n.transpose(numbers)

with open("test.csv", "w" , newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Заголовок 1","Заголовок 2","Заголовок 3","Заголовок 4"])
    writer.writerows(numbers)