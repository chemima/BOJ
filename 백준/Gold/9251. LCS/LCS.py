def lcs_length(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
                if i == 0 or j == 0 :
                    dp[i][j] = 0
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j]= dp[i - 1][j - 1] + 1
                else:
                    dp[i][j]= max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# 입력 받기
str1 = input()
str2 = input()

# LCS 길이 계산 및 출력
result = lcs_length(str1, str2)
print(result)
