import sys
input = sys.stdin.readline

nums = []
sums = []
num = 0
n = int(input().rstrip())
for _ in range(n):
    command = input().split()
    if command[0] == "1":
        if num == 0:
            nums.append(int(command[1]))
            sums.append(int(command[1]))
            num += 1
        else:
            nums.append(int(command[1]))
            sums.append(sums[num-1]+int(command[1]))
            num += 1
    else:
        mid = (num//2) -1
        if sums[mid] <= (sums[-1] -sums[mid]):
            a = sums[mid]
            print(a)
            nums = nums[mid+1:]
            sums = sums[mid+1:]
            for i in range(len(sums)):
                sums[i] -= a
            num = num - mid-1
        
        elif sums[mid] > (sums[-1] -sums[mid]):
            print(sums[-1] -sums[mid])
            nums = nums[:mid+1]
            sums = sums[:mid+1]
            num = mid+1
print(*nums)