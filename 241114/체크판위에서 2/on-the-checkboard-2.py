def backtracking(curr, n):
    global cnt
    if curr == (r-1, c-1):
        if n == 3:
            cnt += 1
            return
    elif curr[0] >= r or curr[1] >= c:
        return
    for i in range(curr[0]+1, r):
        for j in range(curr[1]+1, c):
            if board[i][j] != board[curr[0]][curr[1]]:
                temp = curr
                curr = (i, j)
                backtracking(curr, n+1)
                curr = temp


r, c = map(int, input().split())
board = [['' for _ in range(c)] for _ in range(r)]
for x in range(r):
    board[x] = [t for t in input().split()]


cnt = 0 

backtracking((0,0), 0)

print(cnt)
