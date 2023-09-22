import sys

s = sys.stdin.readline().strip()

maximum = 0
already = 0
s = s.upper()
did = []

for i in range(len(s)):
    if s[i] not in did:
        did.append(s[i])
        if s.count(s[i]) > maximum:
            already = 0
            maximum = s.count(s[i])
            max_s = s[i]

        elif s.count(s[i]) == maximum:
            already = 1 

if already == 1:
    print("?")
else:
    print(max_s)