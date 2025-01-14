import sys
input = sys.stdin.readline

n,k = map(int,input().split())

base = input().rstrip()
ans = []

for i in range(len(base)):
    base_num = ord(base[i])-65
    
    if i == len(base)-1:
        k %= 26
        base_num += k
        base_num %= 26
        ans.append(str(chr(base_num+65)))
        break

    # can spin
    if base_num == 0:
        ans.append("A")
    elif (26-base_num) <=k:
        ans.append("A")
        k -= (26-base_num)
    else:
        ans.append(base[i])
        
for i in ans:
    print(i,end = '')