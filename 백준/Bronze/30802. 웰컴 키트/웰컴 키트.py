import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
T, P = map(int,input().split())
sums = 0

for i in nums:
    if i%T == 0:
        sums += (i//T)
    else:
        sums += (i//T +1)
print(sums)
print(N//P, N%P)
        

