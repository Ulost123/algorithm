import sys
from collections import Counter

n = int(sys.stdin.readline())

n_lst = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline())

m_lst = list(map(int, sys.stdin.readline().strip().split()))

dic = Counter(n_lst)

for i in range(m):
    print(dic[m_lst[i]], end = " ")