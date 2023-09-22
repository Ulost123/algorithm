import sys

m, n = map(int, sys.stdin.readline().strip().split())

def check(n):
    if n == 1: 
        return 0
    else:        
        for i in range(2, int(n ** (0.5) + 1)):
            if n % i == 0:
                return 0 
        return 1 

for i in range(m, n + 1):
    if check(i):
        print(i)
