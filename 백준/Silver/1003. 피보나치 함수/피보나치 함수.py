import sys
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    n = int(input())
    a, b = 1, 0
    for i in range(n):
        a,b = b, a+b 
    print(a,b)