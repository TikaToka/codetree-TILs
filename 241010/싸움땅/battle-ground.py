dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def check(node):
    (x, y) = node
    return 0<=x<n and 0<=y<n

n, m, k = map(int, input().split())

gunBoard = [[[] for _ in range(n)] for _ in range(n)]
humanBoard = [[0 for _ in range(n)] for _ in range(n)]
human = []
hWay = []
hPoint = []
answer = [0 for _ in range(m)]

for i in range(n):
    inp = input().split()
    for j in range(n):
        if int(inp[j]) > 0:
            gunBoard[i][j].append(int(inp[j]))

for i in range(m):
    x, y, d, s = map(int,input().split())
    human.append((x-1, y-1))
    hWay.append(d)
    hPoint.append([s, 0])

for turn in range(k):
    # print(human)
    for i in range(len(human)):
        (x, y), d = human[i], hWay[i]
        nx, ny = x + dx[d], y + dy[d]
        if not(check((nx, ny))):
            hWay[i] = (d + 2) % 4
            nx, ny = x + dx[hWay[i]], y + dy[hWay[i]]
        human[i] = (nx, ny)
        # check human
        idx =-1
        for j in range(len(human)):
                if (nx, ny) == human[j] and i != j:
                    idx = j
                    break

        if idx > -1:
            j = idx
            if sum(hPoint[j]) < sum(hPoint[i]) or (sum(hPoint[j]) == sum(hPoint[i]) and hPoint[j][0] < hPoint[i][0]):
                # add point
                answer[i] += sum(hPoint[i]) - sum(hPoint[j])
                # drop gun
                if hPoint[j][1] != 0:
                    gunBoard[nx][ny].append(hPoint[j][1])
                    hPoint[j][1] = 0
                # j set move
                (x, y), d = human[j], hWay[j]
                for k in range(4):
                    tx, ty = x + dx[(d+k)%4], y + dy[(d+k)%4]
                    if (check((tx, ty))) and (tx, ty) not in human:
                        # j move and get gun
                        human[j] = (tx, ty)
                        hWay[j] = (d+k)%4
                        if len(gunBoard[tx][ty]) != 0:
                            hPoint[j][1] = max(gunBoard[tx][ty])
                            gunBoard[tx][ty].remove(hPoint[j][1])
                        break
                # i change gun
                if gunBoard[nx][ny]:
                    if max(gunBoard[nx][ny]) > hPoint[i][1]:
                        gunBoard[nx][ny].append(hPoint[i][1])
                        hPoint[i][1] = max(gunBoard[nx][ny])
                        gunBoard[nx][ny].remove(hPoint[i][1])

            elif sum(hPoint[j]) > sum(hPoint[i]) or (sum(hPoint[j]) == sum(hPoint[i]) and hPoint[j][0] > hPoint[i][0]):
                # j add point
                answer[j] += sum(hPoint[j]) - sum(hPoint[i])
                # i drop gun
                if hPoint[i][1] != 0:
                    gunBoard[nx][ny].append(hPoint[i][1])
                    hPoint[i][1] = 0
                # i choose way
                (x, y), d = human[i], hWay[i]
                for k in range(4):
                    tx, ty = x + dx[(d+k)%4], y + dy[(d+k)%4]
                    if (check((tx, ty))) and (tx, ty) not in human:
                        # i move and change
                        human[i] = (tx, ty)
                        hWay[i] = (d+k)%4
                        if len(gunBoard[tx][ty]) != 0:
                            hPoint[i][1] = max(gunBoard[tx][ty])
                            gunBoard[tx][ty].remove(hPoint[i][1])
                        break
                # j change
                if gunBoard[nx][ny]:
                    if max(gunBoard[nx][ny]) > hPoint[j][1]:
                        gunBoard[nx][ny].append(hPoint[j][1])
                        hPoint[j][1] = max(gunBoard[nx][ny])
                        gunBoard[nx][ny].remove(hPoint[j][1])

            # check gun
        elif len(gunBoard[nx][ny]) > 0:
            if hPoint[i][1] == 0:
                hPoint[i][1] = max(gunBoard[nx][ny])
                gunBoard[nx][ny].remove(hPoint[i][1])
            else:
                if hPoint[i][1] < max(gunBoard[nx][ny]):
                    gunBoard[nx][ny].append(hPoint[i][1])
                    hPoint[i][1] = max(gunBoard[nx][ny])
                    gunBoard[nx][ny].remove(hPoint[i][1])

            
        # print(human)
        # print(hPoint)
        # print(gunBoard)
        # print('.')
print(' '.join([str(x) for x in answer]))