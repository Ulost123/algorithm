import sys

N = int(sys.stdin.readline())

p_lst = list(map(int, sys.stdin.readline().split()))

p_lst = sorted(p_lst)

res = 0

for i in range(N):
    res = res + p_lst[i]
    for j in range(0,i):
        res += p_lst[j]

print(res)