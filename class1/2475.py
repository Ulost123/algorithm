import sys

lst = list(map(int, sys.stdin.readline().strip().split()))

ans = 0 
for i in range(len(lst)):
    ans += lst[i] ** 2

ans %= 10

print(ans)