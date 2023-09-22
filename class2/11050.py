from math import factorial
import sys

n, k = map(int, sys.stdin.readline().strip().split())

ans = 1
for i in range(k):
    ans = ans * n
    n -= 1 

ans = ans // factorial(k) 

print(ans)