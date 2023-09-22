import sys
from collections import deque

t = int(sys.stdin.readline())

def check(idx, lst):
    idx_lst = [i for i in range(len(lst))]
    #중요도 확인
    cur = 0 
    while cur < len(lst):
        plus = 0
        for i in range(cur, len(lst)):
            if lst[i] > lst[cur]:
                plus = 0 
                lst.append(lst[cur])
                lst.pop(cur)
                idx_lst.append(idx_lst[cur])
                idx_lst.pop(cur)
                break
            else:
                plus = 1
        if plus == 1:
            cur += 1
    return idx_lst.index(idx) + 1

for i in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    docs = list(map(int, sys.stdin.readline().strip().split()))
    print(check(m, docs))
    