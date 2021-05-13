from Product import Product
import random as r
import math

maxMoney = 7000
minMoney = 1

minPopulation = 0

countChar = 4

product_list = []
population = []

k = 5
populationSize = 10
norm = [300, 300, 300]


def generateChromosome():
    chromosome = ""
    for i in range(populationSize):
        chromosome += str(r.randint(0, 1))
    return chromosome


for i in range(populationSize):
    product_list.append(Product(i, countChar))
    population.append(generateChromosome())


def CountSum():
    result = []
    for i in range(len(population)):
        sum = 0
        for j in range(len(population[i])):
            for char in product_list[j].data:
                sum += int(population[i][j]) * char
        result.append(sum)
    return result


def countPrice(str):
    result = 0
    for i in range(len(str)):
        result += product_list[i].price * int(str[i])
    return result


def CountNorm():
    norm_sum = 0
    for i in norm:
        norm_sum += i
    return norm_sum


def CountDeviation(sumList, norm):
    result = []
    for i in range(len(sumList)):
        result.append(sumList[i] - norm)
    return result


def CheckMin(list):
    min = math.fabs(list[0])
    index = 0
    for i in range(len(list)):
        if minMoney < countPrice(population[i]) < maxMoney:
            if math.fabs(list[i]) < min:
                if population[i].count('1') == k:
                    min = math.fabs(list[i])
                    index = i
    print(f'Особь с минимальной разницей--{population[index]}-- {min}')
    return min


def NewPopulation():
    for i in range(len(population)):
        population.append(population[i][0:5] + population[i + 1][5:10])
    print(f'--Новая популяция с кол-вом особей: {i}')


def PopulationForse():
    population[0] = int(population[0], 2) + 1
    b = ''
    while population[0] > 0:
        b = str(population[0] % 2) + b
        population[0] = population[0] // 2
    if len(b) < populationSize:
        b = (populationSize - len(b)) * '0' + b
    population[0] = b


def CheckMinPer(str , min):
    result = 0
    if minMoney < countPrice(str) < maxMoney:
        if str.count('1') == k:
            for i in range(len(str)):
                for char in product_list[i].data:
                    result += int(str[i]) * char
            result = math.fabs(result - CountNorm())
            if result < min:
                min = result
                print(f' {str} --   {min}')
    return min


def checkMinPerFirstTime(str):
    result = 0
    for i in range(len(str)):
        for char in product_list[i].data:
            result += int(str[i]) * char
    result = math.fabs(result - CountNorm())
    return result


trigger = True
iterationPopulation = 0


while trigger:
    minPopulation = CheckMin(CountDeviation(CountSum(), CountNorm()))
    NewPopulation()
    if minPopulation == CheckMin(CountDeviation(CountSum(), CountNorm())):
        iterationPopulation += 1
    else:
        iterationPopulation = 0
    if iterationPopulation == 10:
        trigger = False

print('_____________Полный перебор_____________')
# полный перебор

population = ['0' * populationSize]
trigger = True

min = checkMinPerFirstTime(population[0])

while trigger:
    PopulationForse()
    min = CheckMinPer(population[0],min)
    if population[0] == '1' * populationSize:
        trigger = False
