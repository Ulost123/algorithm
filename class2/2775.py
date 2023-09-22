import sys 

t = int(sys.stdin.readline())

for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline()) 

    p_lst = [i for i in range(1, n + 1)]
    ans_lst = [0 for i in range(n)]
    
    for i in range(k):
        sum = 0
        for j in range(n):
            sum += p_lst[j]
            ans_lst[j] = sum 
        p_lst = ans_lst
        

    print(ans_lst[n-1])


        