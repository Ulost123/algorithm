import sys

t = int(sys.stdin.readline())

def isPalindrome(s, l, r, time):
    time += 1 
    if l >= r:
        return 1, time 
    elif s[l] != s[r]:
        return 0, time
    
    else:
        return isPalindrome(s, l+1, r-1, time)
    
for i in range(t):
    s = sys.stdin.readline().strip()
    a, b = map(int, isPalindrome(s, 0, len(s)-1, 0))
    print(a, b)