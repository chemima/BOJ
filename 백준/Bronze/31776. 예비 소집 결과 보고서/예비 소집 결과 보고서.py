import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    a,b,c = tuple(map(int,input().split()))
    if a == -1:
        continue
    elif (b == -1) and ( c != -1):
        continue
    if (a<=b) and (b<=c) :
        ans += 1
    elif (b == -1) and (c==-1):
        ans += 1
    elif (a<=b) and (c == -1):
        ans += 1
print(ans)