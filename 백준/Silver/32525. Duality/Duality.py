import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    for j in range(N):
        x, y = map(int,input().split())
        print(j+1, x+1, y+500000000)