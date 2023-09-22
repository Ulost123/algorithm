import sys

while 1:
    a = sys.stdin.readline().strip()
    lst = list(map(int, a.split()))
    if a == '0 0 0':
        break 
    lst.sort()
    if lst[2] ** 2 == lst[0] ** 2 + lst[1] ** 2:
        print('right')
    else:
        print('wrong')
