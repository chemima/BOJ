a, b = map(int,input().split())
non_hear = []
non_see = []

for i in range(a):
    person = input()
    non_hear.append(person)
    
for i in range(b):
    person = input()
    non_see.append(person)
    
non_hear_see = list(set(non_hear).intersection(non_see))
non_hear_see.sort()

print(len(non_hear_see))
for _ in range(len(non_hear_see)):
    print(non_hear_see[_])
