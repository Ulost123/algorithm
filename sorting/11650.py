import sys

N = int(sys.stdin.readline())

d_lst = [] 

for i in range(N):
    d = list(map(int, sys.stdin.readline().split()))
    d_lst.append(d)

d_lst.sort()

for i in range(N):
    print(d_lst[i][0], d_lst[i][1])