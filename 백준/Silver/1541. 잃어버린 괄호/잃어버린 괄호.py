import sys
input = sys.stdin.readline
list1 = input().split('-')
sum_ = []

for i in list1:
    sum1 = 0
    temp = i.split('+')
    for j in temp:
        sum1 += int(j)
    sum_.append(sum1)

n = sum_[0]

for i in range(1,len(sum_)):
    n -= sum_[i]
print(n)