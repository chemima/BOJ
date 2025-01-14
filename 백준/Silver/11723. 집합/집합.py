import sys
input = sys.stdin.readline

M = int(input())
S = set()

for i in range(M):
    string = input().strip().split()

    if string[0] == "all":
        S = set(range(1, 21))

    elif string[0] == "empty":
        S.clear()

    else: 
        _, x = string[0], string[1]
        x = int(x)
        
        if _ == "add":
            S.add(x)

        elif _ == "remove":
            S.discard(x)

        elif _ == "check":
            print(1 if x in S else 0)

        elif _ == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)