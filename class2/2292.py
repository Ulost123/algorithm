import sys 
from collections import deque

n = int(sys.stdin.readline())


cur = 1

while 1:
    summation = cur * (cur - 1) / 2 
    end_n = 1 + 6 * summation
    if n <= end_n:
        break
    cur += 1 


print(cur)

