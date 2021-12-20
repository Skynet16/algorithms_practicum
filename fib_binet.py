import math

def fib(n):
    x = ((1 + math.sqrt(5)) / 2) ** n
    y = ((1 - math.sqrt(5)) / 2) ** n
    z = (x - y) / math.sqrt(5)
    return z

result = fib(int(input()))
print(round(result))