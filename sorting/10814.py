import sys

n = int(sys.stdin.readline())

p_lst = []

for i in range(n):
    p = list(sys.stdin.readline().split())
    p[0] = int(p[0])
    p.append(i)
    p_lst.append(p)

p_lst.sort(key = lambda x : (x[0], x[2]))

for i in range(n):
    print(p_lst[i][0], p_lst[i][1])
    