import sys

n, m, v = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(n)]

for i in range(m):
    info = list(map(int, sys.stdin.readline().strip().split()))
    graph[info[0] - 1].append(info[1] - 1)
    graph[info[1] - 1].append(info[0] - 1)

visited_d = [0 for _ in range(n)]
visited_b = [0 for _ in range(n)]

def dfs(v, visited):
    st = [] 
    st.append(v-1)
    visited[v-1] = 1
    print(v, end = ' ')

    while st:
        next = graph[st[-1]]
        next.sort()
        if next:
            b = 0 
            for i in range(len(next)):
                if not visited[next[i]]:
                    visited[next[i]] = 1 
                    st.append(next[i])
                    print(next[i] + 1, end = ' ')
                    b = 1
                    break
            if b == 0:
                st.pop(-1)
        else:
            st.pop(-1)

    return 0

def bfs(v, visited):
    q = [] 
    q.append(v-1)
    visited[v-1] = 1
    print(v, end = ' ')

    while q:
        next = graph[q[0]]
        next.sort()
        if next:
            b = 0
            for i in range(len(next)):
                if not visited[next[i]]:
                    q.append(next[i])
                    visited[next[i]] = 1
                    print(next[i] + 1, end = ' ')
                    b = 1
        q.pop(0)

dfs(v, visited_d)
print()
bfs(v, visited_b)