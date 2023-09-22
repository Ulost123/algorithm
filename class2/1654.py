import sys

k, n = map(int, sys.stdin.readline().strip().split())

line_lst = []

for i in range(k):
    line = int(sys.stdin.readline())
    line_lst.append(line)

start = 1
end = max(line_lst)+1

while start < end:
    mid = (start + end) // 2 
    res = 0 

    for i in range(k):
        res += line_lst[i] // mid

    if res < n:
        end = mid
    else:
        start = mid + 1

print(end-1)