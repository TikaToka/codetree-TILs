import math

def rotate(a, b):
    for i in range(3):
        for j in range(3):
            board[a+i][b+j] = board[3-t-i]

def distance(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return math.abs(x1-x2) + math.abs(y1-y2)

N, M, K = map(int, input())

board = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    board[i] = [int(x) for x in input().split()]

for i in range(M):


ex, ey = map(int, input().split())
    
for i in range(K)