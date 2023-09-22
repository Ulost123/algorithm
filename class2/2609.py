import sys

a, b = map(int, sys.stdin.readline().strip().split())

def big(a, b):
    big_i = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            big_i = i 
    return big_i

def small(a,b):
    n = big(a,b)
    return n * (a // n) * (b // n)

print(big(a,b))
print(small(a,b))