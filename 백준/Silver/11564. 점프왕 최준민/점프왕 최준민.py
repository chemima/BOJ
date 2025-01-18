import sys
input = sys.stdin.readline

k, a, b = map(int, input().split())

if a==0 or b==0 or (a<0 and b>0):
    print(1+ abs(a)//k + abs(b)//k)

else:
    a = abs(a)
    b = abs(b)
    
    if a > b:
        a, b = b, a
        
    ans = (b//k - a//k)
    if a % k == 0:
        ans +=1
    print(ans)