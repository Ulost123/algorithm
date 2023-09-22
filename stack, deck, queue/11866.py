import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

q = []

for i in range(1, n+1):
    q.append(i)
ans = []
print("<", end="")

idx = 0

while len(q) > 0:
    idx += k-1

    if idx > len(q) - 1:
        idx %= len(q)

    num = q.pop(idx)
    ans.append(num)

for i in range(n-1):
    print(ans[i],end=", ")
print(ans[-1], end = "")
print(">")
