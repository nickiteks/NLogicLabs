import math
from bloom import BloomFilter
import docx2txt
import time

m1 = int((-5000 * math.log(0.1)) / pow(math.log(2), 2))
m2 = int((-10000 * math.log(0.5)) / pow(math.log(2), 2))

k1 = int((m1 / 5000) * math.log(2))
k2 = int((m1 / 10000) * math.log(2))

print(m1, m2, k1, k2)
a = [BloomFilter(m1, k1), BloomFilter(m2, k2)]

startTime = time.perf_counter_ns()
text = docx2txt.process("gg.docx")
for word in text.split():
    a[0].addWord(word)
    a[1].addWord(word)
print(f'Время выполнения add: {(time.perf_counter_ns() - startTime)}')

startTime = time.perf_counter_ns()
for word in text.split():
    if word == "роза":
        print(f'Время выполнения поиска: {(time.perf_counter_ns() - startTime)}')

for bl in a:
    startTime = time.perf_counter_ns()
    print(bl.findWord("роза"))
    print()
    print(f'Время выполнения: {(time.perf_counter_ns() - startTime)}\n')
