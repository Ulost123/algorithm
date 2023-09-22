import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().strip().split())

c_lst = list(map(int, sys.stdin.readline().strip().split()))
comb = list(combinations(c_lst, 3))
max_sum = 0 
for i in range(len(comb)):
    cur = comb[i]
    sum = 0
    for j in range(3):
        sum += cur[j]
    if sum > max_sum and sum <= m:
        max_sum = sum

print(max_sum)