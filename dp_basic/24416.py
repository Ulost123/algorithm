import sys 

n = int(sys.stdin.readline())

def fibo_recur(n, cnt):
    if n == 1 or n == 2:
        cnt += 1 
        print(cnt)
        return 1
    else:
        return fibo_recur(n - 1, cnt) + fibo_recur(n - 2, cnt)
    
def fibo_dp(n, cnt):
    f = [0 for i in range(n)]
    f[0], f[1] = 1, 1

    for i in range(2, n):
        cnt += 1 
        f[i] = f[i-1] + f[i-2]

    print(cnt)
cnt_1 = 0
cnt_2 = 0

fibo_recur(n, cnt_1)
fibo_dp(n, cnt_2)

print(cnt_1, cnt_2)

