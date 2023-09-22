import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().strip().split()))

def prime_num(n):
    ans = 0

    if n == 1: 
        return ans 
    elif n == 2:
        ans = 1
        return ans 
    else:
        for i in range(2, n):
            if n % i == 0:
                ans = 0 
                break
            else:
                ans = 1
        return ans 
    
answer = 0 
for i in range(n):
    if prime_num(lst[i]):
        answer += 1
    
print(answer)