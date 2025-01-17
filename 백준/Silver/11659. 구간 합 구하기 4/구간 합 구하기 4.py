import sys
input=sys.stdin.readline

N, M = map(int,input().split())

nums = list(map(int,input().split()))
temp = [0]
sum_ = 0

for i in range(N):
    sum_+= nums[i]
    temp.append(sum_)

for i in range(M):
    start, end = map(int,input().split())
    print(temp[end]-temp[start-1])