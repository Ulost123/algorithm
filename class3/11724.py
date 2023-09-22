import sys 

n, m = map(int, sys.stdin.readline().strip().split())

graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, visited, start):
    st = [] 
    st.append(start)
    visited[start] = 1
    while st:
        next_lst = graph[st[-1]]
        find = 0
        for i in range(len(next_lst)):
            next = next_lst[i] 
            if visited[next] == 0:
                find = 1 
                visited[next] = 1 
                st.append(next)
                break 
        if find == 0:
            st.pop(-1)
    return 1

cnt = 0
for i in range(1, n+1):
    if visited[i] == 0:
        cnt += dfs(graph, visited, i)

print(cnt)
