import time

def fib(n):
    if n <=2:
        return 1
    else:
        prev = 0
        next = 1
        for i in range (0,n):
            temp = next
            next = prev + next
            prev = temp
            i = i + 1
        return prev

starttime = time.time()
result = fib(int(input()))
endtime = time.time() - starttime

print(result,endtime)