import sys

t = int(sys.stdin.readline())

def solution(lst, order):
    r = 0

    for i in range(len(order)):

        if len(lst) == 0:
            zero = 1
        else:
            zero = 0

        if order[i] == 'R':
            if r == 0:
                r = 1 
            else:
                r = 0
        else:
            if zero == 1:
                return -1 
            else:
                if r == 1:
                    lst.pop(-1)
                else:
                    lst.pop(0)
    if r == 1:
        return lst[-1:-len(lst)-1:-1]
    else:
        return lst

        
for i in range(t):
    order = sys.stdin.readline().rstrip()
    m = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()
    if len(arr) > 2:
        arr = list(map(int, arr[1:len(arr)-1].split(",")))
    else:
        arr = [] 

    ans = solution(arr, order)

    if ans == -1:
        print('error')
    else:
        if len(ans) > 1:
            print('[', end = '')
            for i in range(len(ans)-1):
                print(ans[i], end=',')
            print(ans[len(ans) - 1], end = ']\n')
        else:
            print(ans)
        