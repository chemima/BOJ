def lcs_length(str1, str2):
    global dp
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

def lcs_string(str1, str2):
    result = []
    a, b = len(str1), len(str2)
    while a > 0 and b > 0:   
        if dp[a][b] == dp[a][b - 1]:
            b -= 1
        elif dp[a][b] == dp [a-1][b]:
            a -= 1
        elif dp[a][b] == dp[a - 1][b - 1] + 1:
            result.append(str1[a-1])
            a -= 1
            b -= 1
                 
    result.reverse()
    return ''.join(result)
        
        

# 입력 받기
str1 = input()
str2 = input()

# LCS 길이 계산 및 출력
result = lcs_length(str1, str2)
origin = lcs_string(str1, str2)
if result == 0:
    print(result)
    
else:
    print(result)
    print(origin)

