import sys
from math import comb
input = sys.stdin.readline

n,k = map(int,input().split())
S = list(input().rstrip())
p_num = [0 for _ in range(n)]
left = 0
right = n-1
ans = 0

while True:
    if left == n:
        print(0)
        sys.exit(0)
    if S[left] != "C":
        left += 1
    else:
        break

while True:
    if right==-1:
        print(0)
        sys.exit(0)
    if S[right] != "P":
        right -= 1
    else:
        break

while (0<=left<right<=(n-1)):
    if k == 0:
        break
    if (S[left] == "C") and (S[right] == "P"):
        S[left] = "P"
        S[right] = "C"
        k -= 1
    if S[left] == "P":
        left +=1
    if S[right] == "C":
        right -= 1
        
if S[0] == "P":
    p_num[0] = 1
else:
    p_num[0] = 0

for i in range(1,n):
    if S[i] == "P":
        p_num[i] = p_num[i-1] +1
    else:
        p_num[i] = p_num[i-1]
        
cnt = 0
for i in range(n-1,-1,-1):
    if cnt == (n-p_num[n-1]):
        break
    if S[i] == "C":
        cnt += 1
        ans += comb(p_num[i],2)
print(ans)