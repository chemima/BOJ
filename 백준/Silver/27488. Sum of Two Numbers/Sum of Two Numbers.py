import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    n = int(input())
    a, b, power = 0, 0, 1
    f = 0

    while n:
        x = n % 10
        n //= 10

        if x % 2: #현재 자릿수 x가 홀수일 경우 f값 변환. -> 이를 통해 홀수를 번갈아가며 a와 b에 나눔
            f = 1 - f

        a += power * ((x + f) // 2)
        b += power * ((x + 1 - f) // 2)
        power *= 10

    print(a, b)
    
'''
a와 b: 문제에서 요구하는 두 숫자.
power: 현재 자릿수를 나타내는 10의 거듭제곱 값. (1, 10, 100, ...)
f: 플래그로 홀수를 처리하기 위한 변수. f=0 or f=1.

'''
