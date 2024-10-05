dsx = (-1, 0, 1, 0)
dsy = (0, 1, -0, -1)

drx = (-1, -1, 0, 1, 1, 1, 0, -1)
dry = (0, 1, 1, 1, 0, -1, -1, -1)

def distance(n1, n2):
    (x1, y1) = n1
    (x2, y2) = n2
    return (x1-x2)**2 + (y1-y2)**2

n, m, p, c, d = map(int, input().split())

def check_inside(node):
    (x, y) = node
    return 1<=x < n+1 and 1<= y < n+1

# 1
rx, ry = map(int, input().split())

santa = [() for _ in range(p)]
alive = [1 for _ in range(p)]
score = [0 for _ in range(p)]
sleep = [0 for _ in range(p)]
board = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(p):
    idx, sx, sy = map(int, input().split())
    santa[idx-1] = (sx, sy)
    board[sx][sy] = 1

for i in range(m):
    # 2
    # rudolph
    #find closest santa
    min_distance = 2 * (n -1) ** 2 + 1
    min_idx = -1
    for s in range(p):
        if alive[s] != 1:
            continue
        dist = distance((rx, ry), santa[s])
        if dist < min_distance:
            min_distance = dist
            min_idx = s
        elif dist == min_distance:
            if santa[min_idx][0] < santa[s][0]:
                min_distance = dist
                min_idx = s
            elif santa[min_idx][0] == santa[s][0]:
                if santa[min_idx][1] < santa[s][1]:
                    min_distance = dist
                    min_idx = s          
    # find way
    way_idx = -1
    max_reduce = -1 
    for w in range(8):
        dx, dy = drx[w], dry[w]
        nx, ny = rx + dx, ry + dy
        if not check_inside((nx, ny)):
            continue
        reduced = min_distance - distance((nx, ny), santa[min_idx])
        if reduced > max_reduce:
            way_idx = w
            max_reduce = reduced
    #move
    rx += drx[way_idx]
    ry += dry[way_idx]

    # print('r', rx, ry)
    #crash
    for s in range(len(santa)):
        if (rx, ry) == santa[s]:
            score[s] += c
            if sleep[s] <= 0:
                sleep[s] = 2
            board[rx][ry] -= 1
            temp = (santa[s][0] + c * drx[way_idx], santa[s][1] + c * dry[way_idx])
            santa[s] = temp
            if not check_inside(temp):
                alive[s] = 0
                break
            else:
                board[temp[0]][temp[1]] += 1
            check_idx = s
            done = False
            while board[temp[0]][temp[1]] == 2:
                for t in range(len(santa)):
                    if alive[t] != 1:
                        continue
                    if temp == santa[t] and t != check_idx:
                        board[temp[0]][temp[1]] -= 1
                        temp = (temp[0] + drx[way_idx], temp[1] + dry[way_idx])
                        if check_inside(temp):
                            board[temp[0]][temp[1]] += 1
                            santa[t] = temp
                            check_idx = t
                        else:
                            alive[t] = 0
                            santa[t] = temp
                        break
            break
    # print('s1', santa)
    # print(alive)
    # 3
    # santa
    for s in range(len(santa)):
        if alive[s] != 1 or sleep[s] >= 1:
            continue
        way = -1
        min_distance = distance(santa[s], (rx, ry)) # -1 or 0
        for w in range(4):
            dx, dy = dsx[w], dsy[w]
            nx, ny = santa[s][0] + dx, santa[s][1] + dy
            if not check_inside((nx, ny)) or (nx, ny) in santa:
                continue
            reduced = distance((rx, ry), (nx,ny))
            if min_distance > reduced:
                way = w
                min_distance = reduced
            elif min_distance == reduced:
                way = min(way, w)
        if way != -1 and min_distance < distance(santa[s], (rx, ry)) :
            board[santa[s][0]][santa[s][1]] -= 1
            santa[s] = (santa[s][0] + dsx[way], santa[s][1] + dsy[way])
            board[santa[s][0]][santa[s][1]] += 1
        # crash
        if (rx, ry) == santa[s]:
            score[s] += d
            board[rx][ry] -= 1
            if sleep[s] <= 0:
                sleep[s] = 2
            temp = (santa[s][0] - d * dsx[way], santa[s][1] - d * dsy[way])
            if not check_inside(temp):
                alive[s] = 0
                santa[s] = temp
                continue
            else:
                board[temp[0]][temp[1]] += 1
            santa[s] = temp
            check_idx = s
            done = False
            while board[temp[0]][temp[1]] == 2:
                for t in range(len(santa)):
                    if alive[t] != 1:
                        continue
                    if temp == santa[t] and t != check_idx:
                        board[temp[0]][temp[1]] -= 1
                        temp = (temp[0] - dsx[way], temp[1] - dsy[way])
                        if check_inside(temp):
                            board[temp[0]][temp[1]] += 1
                            santa[t] = temp
                            check_idx = t
                        else:
                            alive[t] = 0
                            santa[t] = temp
                        break
    # print('s', santa)
    # print(alive)
    if sum(alive) == 0:
        break
    sleep = [x - 1 for x in sleep]
    for s in range(len(santa)):
        if alive[s] == 1:
            score[s] += 1
    # print(score)
    
        
score = [str(x) for x in score]
print(' '.join(score))