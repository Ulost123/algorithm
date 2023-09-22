import sys

n = int(sys.stdin.readline())
r = 31 

ch_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
val = [i for i in range(1,27)]
dic = dict()

for i in range(26):
    dic[ch_lst[i]] = val[i]

st = sys.stdin.readline().strip()

sum = 0

for i in range(n):
    sum += dic[st[i]] * (r ** i)

print(sum)