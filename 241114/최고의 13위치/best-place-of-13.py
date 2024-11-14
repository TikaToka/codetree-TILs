n = int(input())
board = [[] for _ in range(n)]

for i in range(n):
    board[i] = [x for x in map(int, input().split())]

answer = 0
for i in range(n):
    for j in range(n-2):
        cnt = sum(board[i][j:j+3])
        answer = max(cnt, answer)

for i in range(n):
    for j in range(n-2):
        cnt = sum([board[x][i] for x in range(j, j+3)])
        answer = max(cnt, answer)
        
print(answer)