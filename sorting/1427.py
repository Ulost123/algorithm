import sys

N = sys.stdin.readline().strip()

N_lst = []

for i in range(len(N)):
    N_lst.append(int(N[i]))

N_lst.sort(reverse = True)

ans = ""
for i in range(len(N)):
    ans += str(N_lst[i])

print(ans)
