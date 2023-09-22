import sys 
from collections import deque

n = int(sys.stdin.readline())

st = []

for i in range(n):
    o = list(map(int, sys.stdin.readline().split()))

    if o[0] ==  1:
        st.append(o[1])

    elif o[0] == 2:
        if len(st) > 0:
            n = st.pop(-1)
            print(n)
        else:
            print(-1)

    elif o[0] == 3:
        print(len(st))

    elif o[0] == 4:
        if len(st) > 0:
            print(0)
        else:
            print(1)
            
    else:
        if len(st) > 0:
            print(st[-1])
        else:
            print(-1)
    

