import sys
input = sys.stdin.readline


N, M = map(int,input().split())
coins = []
for i in range(N):
    coin = int(input())
    coins.append(coin)

T=0

for i in range(N-1, -1, -1):
    coin_now = coins[i]
    T += M // coin_now
    M = M % coin_now
    
    if M == 0:
        print(T)
        break
        



