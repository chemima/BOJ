import sys

M, N = map(int,sys.stdin.readline().split())

passwords = {}
for i in range(M):
    a, b = sys.stdin.readline().split()
    passwords[a]=b

for i in range(N):
    input_=sys.stdin.readline().strip()
    print(passwords[input_])
