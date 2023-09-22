import sys

m,n = map(int, sys.stdin.readline().strip().split())

board = []

a_b_1 = ["WBWBWBWB","BWBWBWBW"]
a_b_2 = ["BWBWBWBW","WBWBWBWB"]

for i in range(m):
    board.append(sys.stdin.readline().strip())

count = [] 
for a in range(m-7):
    for b in range(n-7):
        time_w = 0
        time_b = 0
        for i in range(a, 8 + a):
            for j in range(b, 8 + b):
                cur = board[i][j]
                if (i + j) % 2 == 0:
                    if cur != 'W':
                        time_w += 1 
                    if cur != 'B':
                        time_b += 1

                else:
                    if cur != 'B':
                        time_w += 1

                    if cur != 'W':
                        time_b += 1
                        
        count.append(min(time_w, time_b))

print(min(count))