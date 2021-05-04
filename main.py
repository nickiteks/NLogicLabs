from Product import Product
import random as r
import math

product_list = []
population = []

populationSize = 10
norm = [10000, 300, 120, 265]
error = [5000, 100, 70, 70]


def generateChromosome():
    chromosome = ""
    for i in range(populationSize):
        chromosome += str(r.randint(0, 1))
    return chromosome


for i in range(populationSize):
    product_list.append(Product(i))
    population.append(generateChromosome())


def CountSum():
    result = []
    for i in range(len(population)):
        result.append([])
        sum_price = 0
        sum_nutritionalValue = 0
        sum_energyValue = 0
        sum_quality = 0
        for j in range(len(product_list)):
            sum_price += int(population[i][j]) * product_list[j].price
            sum_nutritionalValue += int(population[i][j]) * product_list[j].nutritionalValue
            sum_energyValue += int(population[i][j]) * product_list[j].energyValue
            sum_quality += int(population[i][j]) * product_list[j].quality
        result[i].append(sum_price)
        result[i].append(sum_nutritionalValue)
        result[i].append(sum_energyValue)
        result[i].append(sum_quality)
    return result


def CountNorm(sum_list):
    result = []
    for i in range(len(sum_list)):
        result.append([])
        for j in range(len(sum_list[i])):
            difference = sum_list[i][j] - norm[j]
            result[i].append(difference)
    return result


def CheckNorm(Norm_list):
    for i in range(len(Norm_list)):
        norm_trigger = 0
        for j in range(len(Norm_list[i])):
            if math.fabs(Norm_list[i][j]) < error[j]:
                norm_trigger += 1
        if norm_trigger == len(Norm_list[i]):
            print(population[i])
            return True
    return False


def CountFit(Norm_list):
    result = []
    for i in range(len(Norm_list)):
        sum = 0
        for j in range(len(Norm_list[i])):
            sum += math.pow(Norm_list[i][j], 2)
        result.append(math.sqrt(sum))
    return result


def NewPopulation():
    for i in range(len(population)):
        population.append(population[i][0:5] + population[i + 1][5:10])
    print(i)


def PopulationForse():
    population[0] = int(population[0], 2) + 1
    b = ''
    while population[0] > 0:
        b = str(population[0] % 2) + b
        population[0] = population[0] // 2
    population[0] = b


trigger = True

while trigger:
    if CheckNorm(CountNorm(CountSum())):
        trigger = False
    else:
        NewPopulation()

# полный перебор

population = ['1' + '0' * (populationSize - 1)]


trigger = True

while trigger:
    if CheckNorm(CountNorm(CountSum())):
        trigger = False
    else:
        PopulationForse()
