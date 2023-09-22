import sys

from collections import deque

n = int(sys.stdin.readline())
q = deque([])

for i in range(n):
    order = sys.stdin.readline().strip().split()
    if len(order) > 1:
        if order[0] == "1":
            q.appendleft(int(order[1]))
        else:
            q.append(int(order[1]))
    else:
        if order[0] == '3':
            if len(q) > 0:
                num = q.popleft()
                print(num)
            else:
                print(-1)

        elif order[0] == '4':
            if len(q) > 0:
                num = q.pop()
                print(num)
            else:
                print(-1)

        elif order[0] == '5':
            print(len(q))

        elif order[0] == '6':
            if len(q) == 0:
                print(1)
            else:
                print(0)

        elif order[0] == '7':
            if len(q) > 0:
                print(q[0])
            else:
                print(-1)

        else:
            if len(q) > 0:
                print(q[-1])
            else:
                print(-1)