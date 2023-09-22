import sys

N = int(sys.stdin.readline())

lst = [sys.stdin.readline().strip() for i in range(N)]

lst = list(set(lst))

lst.sort()
# sorting by length of word

lst.sort(key = lambda x : len(x))

for i in range(len(lst)):
    print(lst[i])