import pandas as p
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = p.read_csv('laba1')

keys = data.keys()
# 0 - CPU ,
# 1 - Количество ядер,
# 2- 'Кэш жесткого диска',
# 3-'Уровень шума жесткого диска'

# --замена шумов--
print(np.nanmedian(data[keys[0]]))
for i in range(0, 3):
    data.loc[(data[keys[i]] - np.nanmedian(data[keys[i]])) / np.nanmedian(
        data[keys[i]]) > 5, keys[i]] = np.nan

for i in range(0, 3):
    data[keys[i]].update(data[keys[i]].replace(np.nan, round(np.nanmean(data[keys[i]]), 1)))

x = data[keys[0]].values.reshape((-1, 1))
y = data[keys[1]].values

model = LinearRegression().fit(x, y)

y_pred = model.predict(x)
print(f'Slope:{model.coef_[0]}')
print(f'Intercept:{model.intercept_}')
print(f'r^2:{model.score(x, y)}')

plt.scatter(x, y)
plt.plot(x, model.predict(x), color='red', linewidth=2)
plt.show()
