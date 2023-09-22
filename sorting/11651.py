import sys

n = int(sys.stdin.readline())

d_lst = []
for i in range(n):
    d = list(map(int, sys.stdin.readline().split()))
    d_lst.append(d)

d_lst.sort(key = lambda x : (x[1], x[0]))

for i in range(n):
    print(d_lst[i][0], d_lst[i][1])