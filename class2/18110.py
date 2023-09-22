import sys
import math

n = int(sys.stdin.readline())

def up(n):
    str_n = str(n)
    for i in range(0, len(str_n)):
        if str_n[i] == '.':
            break
    if int(str_n[:i]) % 2 == 0 and int(str_n[i+1]) >= 5:
        return math.ceil(n)
    return round(n)

print(up(1.5))

if n != 0:
    ghost = n * 0.3 * 0.5

    ghost = up(ghost)

    s_lst = [] 

    for i in range(n):
        s_lst.append(int(sys.stdin.readline()))

    s_lst.sort()

    s_lst[ghost:n-ghost+1]

    print(up(sum(s_lst[ghost:n-ghost]) / len(s_lst[ghost:n-ghost])))
