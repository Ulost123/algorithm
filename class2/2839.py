import sys

n = int(sys.stdin.readline())

ans_lst = []

for i in range(0, n // 3 + 1):
    cur = 3 * i
    for j in range(0, n // 5 + 1):
        sum = 3 * i + 5 * j
        if sum == n:
            ans_lst.append(i+j)
            break
        elif sum > n:
            break

if len(ans_lst):
    print(min(ans_lst))

else:
    print(-1)


