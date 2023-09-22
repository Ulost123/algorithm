import sys

m, n, h = map(int,sys.stdin.readline().strip().split())

visited = [[[0 for _ in range(m)] for __ in range(n)] for ___ in range(h)]
id_lst = []

zero_cnt = 0
for i in range(h):
    for j in range(n):
        tom = list(map(int, sys.stdin.readline().strip().split()))
        visited[i][j] = tom 
        for k in range(m):
            if tom[k] == 1:
                id_lst.append([i, j, k])
            if tom[k] == 0:
                zero_cnt += 1

def solution(visited, id_lst, zero_cnt):
    q = id_lst  
    cnt = 0 
    cnt_did = 0
    while q:
        len_q = len(q)
        for i in range(len_q):
            # 위 아래 앞 뒤 양 옆 
            cur_idx = q.pop(0)
            i_h = cur_idx[0]
            i_n = cur_idx[1]
            i_m = cur_idx[2]

            if (i_h - 1) >= 0 and visited[i_h - 1][i_n][i_m] == 0:
                visited[i_h - 1][i_n][i_m] = 1
                q.append([i_h - 1, i_n, i_m])
                cnt_did += 1

            if (i_h + 1) < h and visited[i_h + 1][i_n][i_m] == 0:
                visited[i_h + 1][i_n][i_m] = 1
                q.append([i_h + 1, i_n, i_m])
                cnt_did += 1

            if i_n - 1 >= 0 and visited[i_h][i_n - 1][i_m] == 0:
                visited[i_h][i_n - 1][i_m] = 1
                q.append([i_h, i_n - 1, i_m])
                cnt_did += 1

            if i_n + 1 < n and visited[i_h][i_n + 1][i_m] == 0:
                visited[i_h][i_n + 1][i_m] = 1
                q.append([i_h, i_n + 1, i_m])
                cnt_did += 1

            if i_m - 1 >= 0 and visited[i_h][i_n][i_m - 1] == 0:
                visited[i_h][i_n][i_m - 1] = 1
                q.append([i_h, i_n, i_m - 1])
                cnt_did += 1 

            if i_m + 1 < m and visited[i_h][i_n][i_m + 1] == 0:
                visited[i_h][i_n][i_m + 1] = 1
                q.append([i_h, i_n, i_m + 1])
                cnt_did += 1

        cnt += 1
    if cnt_did != zero_cnt:
        return -1
    else:
        return cnt - 1

ans = solution(visited, id_lst, zero_cnt)

print(ans)