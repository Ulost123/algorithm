import sys
from math import factorial

n = int(sys.stdin.readline())

f = factorial(n)

st_f = str(f)

cnt = 0

for i in range(len(st_f)-1, -1, -1):
    if st_f[i] == '0':
        cnt += 1

    else:
        break

print(cnt)