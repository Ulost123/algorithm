import sys
from collections import deque
m, n= map(int,sys.stdin.readline().strip().split())

visited = [[0 for _ in range(m)] for __ in range(n)]
id_lst = []

zero_cnt = 0
for i in range(n):
    tom = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(m):
        visited[i][j] = tom[j]
        if tom[j] == 1:
            id_lst.append([i, j])
        if tom[j] == 0:
            zero_cnt += 1

def solution(visited, id_lst, zero_cnt):
    q = deque(id_lst)
    cnt = 0 
    cnt_did = 0
    while q:
        len_q = len(q)
        for i in range(len_q):
            # 위 아래 앞 뒤 양 옆 
            cur_idx = q.popleft()
            i_n = cur_idx[0]
            i_m = cur_idx[1]

            if i_n - 1 >= 0 and visited[i_n - 1][i_m] == 0:
                visited[i_n - 1][i_m] = 1
                q.append([i_n - 1, i_m])
                cnt_did += 1

            if i_n + 1 < n and visited[i_n + 1][i_m] == 0:
                visited[i_n + 1][i_m] = 1
                q.append([i_n + 1, i_m])
                cnt_did += 1

            if i_m - 1 >= 0 and visited[i_n][i_m - 1] == 0:
                visited[i_n][i_m - 1] = 1
                q.append([i_n, i_m - 1])
                cnt_did += 1 

            if i_m + 1 < m and visited[i_n][i_m + 1] == 0:
                visited[i_n][i_m + 1] = 1
                q.append([i_n, i_m + 1])
                cnt_did += 1

        cnt += 1
    if cnt_did != zero_cnt:
        return -1
    else:
        return cnt - 1

ans = solution(visited, id_lst, zero_cnt)

print(ans)