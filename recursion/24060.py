import sys

n, k = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

def merge_sort(lst, p, r):
    if p < r:
        q = (p + r) / 2
        merge_sort(lst, p, q)
        merge_sort(lst, q+1, r)
        merge(lst, p, q, r)

def merge(lst, p, q, r):
    tmp = 
    i = p
    j = q+1
    t = 0
    while i <= q and j <= r:
        if lst[i] <= lst[j]:
