import sys 

n, m, b = map(int, sys.stdin.readline().strip().split())

lst = []

for i in range(n):
    lst.extend(map(int, sys.stdin.readline().strip().split()))

dic={}

for i in lst:
    if i not in dic:
        dic[i] = 1 

    else:
        dic[i] += 1

time = sys.maxsize
height = 0

for i in range(min(lst), max(lst)+1): 
    t = 0 
    tb = b 

    for j in dic:
        q = dic.get(j)

        if j > i: 
            t += (j - i) * q * 2 
            tb += (j - i) * q 
        
        else:
            t += (i - j) * q  
            tb -= (i - j) * q 
            
    if tb >= 0:     
        if t <= time: 
            time = t
            height = i

print(time, height)