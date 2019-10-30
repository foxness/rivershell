import random
from collections import Counter
import itertools

def rand():
  while True:
    yield random.randint(1, 100)

def calcExpected(a):
  expected = 0

  for num, count in dict(Counter(a)).items():
    probability = count / len(a)
    expected += probability * num

  return expected

def getVariance(n, seq):
  buff = []

  for s in seq:
    buff.append(s)

    if len(buff) == n:
      variance = 0
      expected = calcExpected(buff)

      for num, count in dict(Counter(buff)).items():
        probability = count / len(buff)
        variance += probability * ((num - expected) ** 2)
      
      yield variance

      buff = buff[1:]

#sequence = [1, 2, 5, 6, 7, 8, 10, 12, 123, 321, 123, 1, 1, 1]
sequence = rand()

print(list(itertools.islice(getVariance(10, sequence), 5)))