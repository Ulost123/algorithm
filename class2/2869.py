import sys

a, b, v = map(int, sys.stdin.readline().strip().split())

up = a - b

print((v-a) // up + 1)