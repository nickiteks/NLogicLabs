from bloom import BloomFilter
import docx2txt
import time

a = [BloomFilter(20000, 2)]

startTime = time.perf_counter_ns()
text = docx2txt.process("gg.docx")
for word in text.split():
    a[0].addWord(word)
print(f'Время выполнения add: {(time.perf_counter_ns() - startTime)}')

startTime = time.perf_counter_ns()
for word in text.split():
    if word == "роза":
        print(f'Время выполнения поиска: {(time.perf_counter_ns() - startTime)}')

for bl in a:
    startTime = time.perf_counter_ns()
    print(bl.findWord("роза"))
    print()
    print(f'Время выполнения: {(time.perf_counter_ns() - startTime)}')