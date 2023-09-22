import sys

n = int(sys.stdin.readline())

p_lst = []
rank_lst = [] 

for _ in range(n):
    p = list(map(int, sys.stdin.readline().strip().split()))
    p_lst.append(p)

for i in range(n):
    rank = 1
    for j in range(n):
        if i != j:
            if p_lst[i][0] < p_lst[j][0] and p_lst[i][1] < p_lst[j][1]:
                rank += 1 
    print(rank, end = ' ')
