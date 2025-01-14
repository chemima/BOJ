import sys

N = int(sys.stdin.readline())

nums = {}
num = list(map(int, sys.stdin.readline().split()))
num1 = sorted(list(set(num)))

for i in range(len(num1)):
    nums[num1[i]]=i


for i in num:
    print(nums[i], end=' ')