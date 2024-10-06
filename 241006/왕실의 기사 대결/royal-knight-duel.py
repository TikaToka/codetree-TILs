L, N, Q = map(int, input().split())

board = [[] for _ in range(L)]
for i in range(L):
    board[i] = [int(x) for x in input.split()]

knight=[]

for i in range(N):
    r, c, h, w, k = map(int, input().split())