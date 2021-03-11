import pandas as p
import numpy as np

data = p.read_csv('laba1')

keys = data.keys()
# 0 - CPU ,
# 1 - Количество ядер,
# 2- 'Кэш жесткого диска',
# 3-'Уровень шума жесткого диска'


dispersion = np.var(data[keys[0]])
mean = np.mean(data[keys[1]])
std = np.std(data[keys[3]])

print(dispersion, mean, std)

# --замена шумов--
print(np.nanmedian(data[keys[0]]))
for i in range(0, 3):
    data.loc[(data[keys[i]] - np.nanmedian(data[keys[i]])) / np.nanmedian(
        data[keys[i]]) > 5 , keys[i]] = np.nan

for i in range(0, 3):
    data[keys[i]].update(data[keys[i]].replace(np.nan, round(np.nanmean(data[keys[i]]), 1)))


dispersion = np.var(data[keys[0]])
mean = np.mean(data[keys[1]])
std = np.std(data[keys[3]])

print(dispersion, mean, std)
