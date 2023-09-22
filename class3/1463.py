import sys 
from collections import deque
n = int(sys.stdin.readline())

d = [0] * (n+1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
for i in range(2, n + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d)


'''
inf = n
way = [[inf for _ in range(n+1)] for __ in range(n+1)]
dp = [inf for _ in range(n+1)]

for i in range(1, n+1):
    a = i * 3
    b = i * 2 
    c = i + 1 
    if a <= n:
        way[i][a] = 1
    if b <= n: 
        way[i][b] = 1
    if c <= n:
        way[i][c] = 1

    if i == 1:
        dp[a] = 1 
        dp[b] = 1
        dp[c] = 1 

for j in range(2, n+1):
    dp[j] = min(way[1][j], dp[j-1] + way[j-1][j])

print(dp)
'''