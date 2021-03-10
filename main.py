import csv
import numpy as np
import random
import pandas as pp
CPU = np.random.poisson(5, 500) * 1.0 #чистый цпу возвращает одномерный массив из указанного количества элементов, значения которых равномерно распределенны внутри заданного интервала


i = 0
for row in CPU:
    if( i < 480):
        p = random.randint(1, 20)
        CPU[i+p] = CPU[i] + 100050
        i += p

i = 0
for row in CPU:
    CPU[i] = CPU[i].round().astype(int)
    if CPU[i] == 1:
        CPU[i] = np.nan #пропуски вот тут
    i += 1

CPUCoreCount = (np.random.randint(0, 8, 500)) # ядра, Массив случайных целых чисел из интервала

i = 0
for row in CPUCoreCount:
    if( i < 480):
        p = random.randint(1, 30)
        CPUCoreCount[i+p] = CPUCoreCount[i] + 100050
        i += p

i = 0
for row in CPUCoreCount:
    CPUCoreCount[i] = CPUCoreCount[i].round().astype(int)
    i += 1

pureCashSata = np.random.randint(0, 4, 500) #Массив случайных целых чисел из интервала
i = 0
for row in pureCashSata:
    if pureCashSata[i] == 1:
        pureCashSata[i] = 16
    elif pureCashSata[i] == 2:
        pureCashSata[i] = 32
    elif pureCashSata[i] == 3:
        pureCashSata[i] = 64
    i += 1

pureNoiseLevelSata = pureCPU = np.linspace(25, 30, 500) #уровень шума возвращает одномерный массив
noiseNoiseLevelSata = np.random.normal(0, 1.5, pureNoiseLevelSata.shape) # случайная выборка
NoiseLevelSata = (pureNoiseLevelSata + noiseNoiseLevelSata)

for row in NoiseLevelSata:
    if( i < 480):
        p = random.randint(1, 20)
        NoiseLevelSata[i+p] = NoiseLevelSata[i] + 100050
        i += p

i = 0

for row in NoiseLevelSata:
    if NoiseLevelSata[i] < 24:
        NoiseLevelSata[i] = np.nan #пропуски
    NoiseLevelSata[i] = round(NoiseLevelSata[i], 3)
    i += 1

dispersion = np.var(CPU)  # дисперсия
mean = np.mean(CPUCoreCount)  # среднее арифмет
std = np.std(NoiseLevelSata)  # стандартное отклонение

print("Дисперсия CPU - ", dispersion)
print("Среднее арифметическое ядер - ", mean)
print("Стандартное отклонение шума жесткого диска - ", std)

zip_list = zip(CPU, CPUCoreCount, pureCashSata, NoiseLevelSata)

df = pp.DataFrame(zip_list, columns = ["CPU", "Количество ядер", "Кэш жесткого диска", "Уровень шума жесткого диска"] )
df.to_csv('laba1', index= False)