import sys

k = int(sys.stdin.readline())

st = [] 

for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        st.pop(-1)
    else:
        st.append(num)

print(sum(st))