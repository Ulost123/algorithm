import sys 

t = int(sys.stdin.readline())

for i in range(t):
    lst = list(map(int, sys.stdin.readline().strip().split()))
    max_floor = lst[0]
    max_num = lst[1]
    n = lst[2]
    room_plus = (n-1) // max_floor
    floor = n % (max_floor)
    if floor == 0:
        floor = max_floor
    ans = floor * 100 + 1 + room_plus
    print(ans)
    