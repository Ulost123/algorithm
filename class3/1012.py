import sys 

def find(plant, visited):

    st = [] 
    x = plant[0]
    y = plant[1]
    st.append([x, y])
    visited[x][y] = 1

    while st:
        next = 0

        cur = st[-1]

        cur_x = cur[0]
        cur_y = cur[1]

        u_x = cur_x - 1
        u_y = cur_y
        
        r_x = cur_x
        r_y = cur_y + 1 

        l_x = cur_x
        l_y = cur_y - 1  
        
        d_x = cur_x + 1 
        d_y = cur_y

        if u_x >= 0:
            if visited[u_x][u_y] == 0 and farm[u_x][u_y] == 1:
                st.append([u_x, u_y])
                visited[u_x][u_y] = 1 
                next = 1
        
        if r_y <= n-1:
            if visited[r_x][r_y] == 0 and farm[r_x][r_y] == 1:
                st.append([r_x, r_y])
                visited[r_x][r_y] = 1 
                next = 1

        if l_y >= 0:
            if visited[l_x][l_y] == 0 and farm[l_x][l_y] == 1:
                st.append([l_x, l_y])
                visited[l_x][l_y] = 1 
                next = 1

        if d_x <= m-1:
            if visited[d_x][d_y] == 0 and farm[d_x][d_y] == 1:
                st.append([d_x, d_y])
                visited[d_x][d_y] = 1 
                next = 1

        if next == 0:
            st.pop(-1)

    return 1  


t = int(sys.stdin.readline())

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())

    farm = [[0 for _ in range(n)] for __ in range(m)]
    visited = [[0 for _ in range(n)] for __ in range(m)]
    plant_lst = [] 

    for i in range(k):
        plant = list(map(int, sys.stdin.readline().strip().split()))
        farm[plant[0]][plant[1]] = 1
        plant_lst.append(plant)


    cnt = 0
    for i in range(len(plant_lst)):
        plant = plant_lst[i]
        if visited[plant[0]][plant[1]] != 1:
            p = find(plant, visited)
            cnt += p 

    print(cnt)
