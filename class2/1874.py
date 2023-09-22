import sys
from collections import deque

n = int(sys.stdin.readline())
pic_lst = []
st = []
cur = 0
find = 1
for i in range(n):
    num = int(sys.stdin.readline())
    if not st:
        if cur <= num:
            for i in range(cur+1, num + 1):
                st.append(i)
                pic_lst.append("+")
            cur = num
            st.pop(-1)
            pic_lst.append("-")
        else:
            find = 0
            break
    else:
        if cur < num:
            for i in range(cur+1, num + 1):
                st.append(i)
                pic_lst.append("+")
            cur = num
            st.pop(-1)
            pic_lst.append("-")
        else:
            a = st[-1]
            if a == num: 
                st.pop(-1)
                pic_lst.append("-")

            else:
                find = 0
                break
if find == 1:
    for i in range(len(pic_lst)):
        print(pic_lst[i])
else:
    print("NO")