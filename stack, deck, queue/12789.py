import sys

n = int(sys.stdin.readline())

num_lst = list(map(int, sys.stdin.readline().split()))

w_lst = [] 

cur_num = 1 
possible = 1

while 1:
    if len(num_lst) > 0:
        c = num_lst[0]
        if c == cur_num:
            num_lst.pop(0)
            cur_num += 1
        else:
            if len(w_lst) > 0:
                n_c = w_lst[len(w_lst) - 1]
                if n_c == cur_num:
                    w_lst.pop(len(w_lst) - 1)
                    cur_num += 1
                else:
                    num_lst.pop(0)
                    w_lst.append(c)
            else:
                num_lst.pop(0)
                w_lst.append(c)

    else:
        c = w_lst.pop(len(w_lst) - 1)
        if c == cur_num:
            cur_num += 1 
        else:
            possible = 0 
            break 

    if len(num_lst) == 0 and len(w_lst) == 0:
        break 

if possible:
    print("Nice")
else:
    print("Sad")