import sys
input = sys.stdin.readline

a, b = map(int,input().split())
non_hear = [0] * a
non_see = [0] * b

for i in range(a):
    person = input().strip()
    non_hear[i] = person
    
for i in range(b):
    person = input().strip()
    non_see[i] = person
    
non_hear_see = list(set(non_hear).intersection(non_see))
non_hear_see.sort()

print(len(non_hear_see))
for _ in range(len(non_hear_see)):
    print(non_hear_see[_])