import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    N = int(input())
    dp = [0] * (N + 1)

    for j in range(1, N + 1):
        if j == 1:
            dp[j] = 1
        elif j == 2:
            dp[j] = 2
        elif j == 3:
            dp[j] = 4
        else:
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    print(dp[N])