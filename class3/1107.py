import sys

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

break_lst = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n, -1, -1):
    str_i = str(i)
    find = 1 
    for j in range(len(str_i)):
        if int(str_i[j]) in break_lst:
            find = 0
            break
    if find == 1:
        break

cand_1 = i 

id = n 

while 1: 
    find = 1 
    for k in range(len(str(id))):
        if int(str(id)[k]) in break_lst:
            find = 0 
            break
    if find == 1 or abs(n-100) < abs(n-id) + len(str(id)):
        break
    id += 1 

cand_2 = id 

if abs(n - cand_1) > abs(n - cand_2):
    standard = cand_2
else:
    standard = cand_1

if abs(n - standard) + len(str(standard)) < abs(n - 100):
    ans = abs(n-standard) + len(str(standard))
else:
    ans = abs(n-100)

print(ans)


