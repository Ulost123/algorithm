import sys

n = int(sys.stdin.readline())

num_lst = [0 for i in range(10001)]

for i in range(n):
    num = int(sys.stdin.readline())
    num_lst[num] += 1

for i in range(len(num_lst)):
    if num_lst[i] != 0:
        for j in range(num_lst[i]):
            print(i)
        
