import sys
from collections import deque

n = int(sys.stdin.readline())

q_st_lst = list(map(int, sys.stdin.readline().split()))

num_lst = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

insert_lst = list(map(int, sys.stdin.readline().split()))

q = deque([])
for i in range(n):
    if q_st_lst[i] == 0:
        q.appendleft(num_lst[i])

for j in range(m):
    q.append(insert_lst[j])
    num = q.popleft()
    print(num, end= " ")
    
