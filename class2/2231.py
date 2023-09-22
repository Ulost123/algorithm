import sys

n = int(sys.stdin.readline())

find = 0
for m in range(1, n):
    m_str = str(m)
    sum = 0 
    for i in range(len(m_str)):
        sum += int(m_str[i])
    sum += m 
    if sum == n:
        find = 1
        break 

if find == 0:
    print(0)

else:
    print(m)