import sys

def binary_search(arr, n):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < n:
            start = mid + 1 
           
        elif arr[mid] > n:
            end = mid - 1
            
        elif arr[mid] == n:
            
            break

    return mid

n = int(sys.stdin.readline())

d_lst = list(map(int, sys.stdin.readline().split()))

sorted_d_lst = sorted(list(set(d_lst)))

ans_lst = [] 

for i in range(n):
    cur = d_lst[i]
    idx = binary_search(sorted_d_lst, cur)
    print(idx, end = " ")
    