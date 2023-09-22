import sys 

def binary_search(arr, n):
    start = 0
    end = len(arr) - 1
    ans = 0

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == n:
            ans = 1 
            break 

        elif arr[mid] < n:
            start = mid + 1
            
        else:
            end = mid -1

    return ans

N = int(sys.stdin.readline())

N_lst = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

M_lst = list(map(int, sys.stdin.readline().split()))

N_idx = 0 

N_lst.sort()

for i in range(M):
    cur = M_lst[i]
    print(binary_search(N_lst, cur))
        
        


