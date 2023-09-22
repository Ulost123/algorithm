import sys

lst = list(map(int, sys.stdin.readline().strip().split()))

asc = 0
dsc = 0 
mix = 0 

for i in range(7):
    if lst[i+1] - lst[i] == 1:
        asc = 1

    elif lst[i+1] - lst[i] == -1:
        dsc = 1

    else:
        asc = 0
        dsc = 0
        mix = 1
        break

if asc:
    print('ascending')

elif dsc: 
    print('descending')

else:
    print('mixed')