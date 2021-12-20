n = int(input())

d = n / 3
f = n // 3
T = "odd"
F = "even"

def fib_eo(n):
	if f < d:
		return T
	else: 
		return F

print(fib_eo(n))