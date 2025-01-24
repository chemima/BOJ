import sys
input = sys.stdin.readline

N = int(input())
time_arr=list(map(int,input().split()))
time_arr.sort()

ans = 0
for i in range(1, N+1):
    ans += sum(time_arr[:i])
print(ans)