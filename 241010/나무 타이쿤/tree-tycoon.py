dx = (0, -1, -1, -1, 0, 1, 1, 1)
dy = (1, 1, 0, -1, -1, -1, 0, 1)

ix = (-1, -1, 1, 1)
iy = (-1, 1, -1, 1)

def check(node):
    return 0<=node[0]<n and 0<=node[1]<n

n, m = map(int, input().split())

board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    board[i] = [x for x in map(int, input().split())]

rules = {}
for i in range(m):
    d, p = map(int, input().split())
    rules[i] = (d-1, p)

medicine = set()
for i in range(2):
    for j in range(2):
        medicine.add((i+n-2, j))
# print(board)
for yrs in range(m):
    # print(yrs)
    d, p = rules[yrs]

    # move
    newMedicine = set()
    for med in medicine:
        (x, y) = med
        (nx, ny) = (x + p * dx[d]) % n, (y + p * dy[d]) % n
        newMedicine.add((nx, ny))
    
    medicine = newMedicine
    # print(medicine)

    # inject and remove (삭제는 뒤에서 함)
    for med in medicine:
        (x, y) = med
        board[x][y] += 1
    # 대각선 나무들 수 만큼 해당 나무 성장 (격자 안에만)
    # print('a',board)
    for med in medicine:
        x, y = med
        cnt = 0
        for k in range(4):
            nx, ny = x + ix[k], y + iy[k]
            if check((nx, ny)) and board[nx][ny] >= 1:
                cnt += 1
        board[x][y] += cnt

    # print('b',board)
    
    
    #  전체에서 안넣은 애들중 높이 2 이상은 2씩 베어서 특수영양제 그 자리에 배치 (높이 0이면 씨앗만있음)
    newMedicine = set()
    for i in range(n):
        for j in range(n):
            if (i, j) not in medicine and board[i][j] >= 2:
                board[i][j] -=2
                newMedicine.add((i, j))
    medicine = newMedicine

    # print(medicine)
    # print(board)


answer = 0
for i in range(n):
    for j in range(n):
        answer += board[i][j]
print(answer)