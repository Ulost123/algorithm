import sys 

n = int(sys.stdin.readline())

sc_lst = [0]
for i in range(n):
    sc_lst.append(int(sys.stdin.readline()))

d = [[0 for i in range(3)] for j in range(n + 1)]

for i in range(1, n + 1):
    d[i][0] = max(d[i-1][1], d[i-1][2])
    d[i][1] = d[i-1][0] + sc_lst[i] 
    d[i][2] = d[i-1][1] + sc_lst[i] 

print(max(d[n][1], d[n][2]))