import sys

def pelindrome(st):
    end = len(st) - 1
    start = 0
    ans = 1

    if len(st) == 1:
        return ans
    
    else:
        while start < end:
            a = st[start]
            b = st[end]
            if a != b:
                ans = 0 
                break 
            start += 1 
            end -= 1 
        return ans
    
while 1:
    n = sys.stdin.readline().strip()
    if n == '0':
        break
    if pelindrome(n):
        print('yes')
    else:
        print('no')