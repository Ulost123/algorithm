import sys

n_lst = [] 

avg = 0 

for i in range(5):
    num = int(sys.stdin.readline())
    avg += num
    n_lst.append(num)

avg //= 5
print(avg)
print(sorted(n_lst)[2])