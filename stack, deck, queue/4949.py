import sys

stack  = [] 

while 1:
    eq = 1
    stack  = [] 
    st = sys.stdin.readline().rstrip()

    if st == ".":
        break

    for i in st:
        if i == "(":
            stack.append(i)

        elif i == ")":
            if len(stack) != 0:
                cmp = stack[-1]
                if cmp != "(":
                    eq = 0
                    break
                
                else:
                    stack.pop(-1)
            else:
                eq = 0
                break

        elif i == "[":
            stack.append(i)
    
        elif i == "]":
            if len(stack) != 0:
                cmp = stack[-1]
                if cmp != "[":
                    eq = 0
                    break
                
                else:
                    stack.pop(-1)

            else:
                eq = 0 
                break
    if len(stack) != 0:
        eq = 0

    if eq == 1:
        print("yes")
    
    else:
        print("no")

