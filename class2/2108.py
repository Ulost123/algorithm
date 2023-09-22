import sys
from collections import Counter

n = int(sys.stdin.readline())
lst = [] 

for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()
mode_lst = Counter(lst).most_common()
if len(mode_lst) > 1:
    if mode_lst[0][1] == mode_lst[1][1]:
        mode = mode_lst[1][0]

    else:
        mode = mode_lst[0][0]
else:
    mode = mode_lst[0][0]

        

print(round(sum(lst) / n))
print(lst[n//2])
print(mode)
print(max(lst) - min(lst))
