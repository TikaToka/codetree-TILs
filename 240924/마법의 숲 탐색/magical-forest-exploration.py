def dfs(graph, start):
    tovisit = []
    visited = []
    row = 0
    tovisit.append(start)
    iterate = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while tovisit:
        node= tovisit.pop()
        visited.append(node)
        row = max(row, node[0])
        if row == len(graph):
            return row
        for dx, dy in iterate:
            tempx, tempy = node[0] + dx, node[1] + dy
            if not (0 <= tempx < r and 0 <= tempy < c):
                continue
            if graph[tempx][tempy] != 0 and [tempx, tempy] not in visited:
                tovisit.append([tempx, tempy])
    return row + 1

def check(curr, look, graph):
    if look == [1, 0]: # S
        todo = [[1, 0], [0, 1], [0, -1]]
    elif look == [0, -1]: # W
        todo = [[1, 0], [0, -1], [-1, 0]]
    elif look == [0, 1]: # E
        todo = [[1, 0], [0, 1], [-1, 0]]
    for dx, dy in todo:
        tx, ty = (curr[0] + dx, curr[1] + dy)
        if tx < 0:
            continue
        if not (tx < r and 0 <= ty < c):
            return False
        elif graph[tx][ty] != 0:
            return False
    return True


answer = 0
r, c, k = map(int, input().split())
graph = [[0 for _ in range(c)] for _ in range(r)]
for v, i in enumerate(range(k)):
    ci, di = map(int, input().split())
    curr = [-2, ci-1]
    look = [1, 0]
    while True:
        # print(curr[0]+1, curr[1]+1, di)
        if curr[0] == r-2:
            break
        # S
        cand = [a + b for a, b in zip(curr, look)]
        if check(cand, look, graph):
            curr = cand
        else: # W
            look = [0, -1]
            cand = [a + b for a, b in zip(curr, look)]
            if check(cand, look, graph):# S
                look = [1, 0]
                cand = [a + b for a, b in zip(cand, look)]
                if check(cand, look, graph):
                    curr = cand
                    di = di - 1 if di - 1 >= 0  else di + 3
                else: # E
                    look = [0, 1]
                    cand = [a + b for a, b in zip(curr, look)]
                    if check(cand, look, graph):# S
                        look = [1, 0]
                        cand = [a + b for a, b in zip(cand, look)]
                        if check(cand, look, graph):
                            curr = cand
                            di = di + 1 if di + 1 < 4 else di - 3
                        else:
                            break
                    else:
                        break
            else: # E
                look = [0, 1]
                cand = [a + b for a, b in zip(curr, look)]
                if check(cand, look, graph):# S
                    look = [1, 0]
                    cand = [a + b for a, b in zip(cand, look)]
                    if check(cand, look, graph):
                        curr = cand
                        di = di + 1 if di + 1 < 4 else di -3
                    else:
                        break
                else:
                    break

    x, y = curr
    # print(x+1, y+1, di)
    test = True
    for idx, (dx, dy) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1], [0, 0]]):
        tempx , tempy = (x + dx, y + dy)
        if not (0 <= x + dx < r and 0 <= y + dy < c):
            graph = [[0 for _ in range(c)] for _ in range(r)]
            test = False
            break
        if idx == di:
            exit = [tempx, tempy]
        graph[tempx][tempy] = v+1
    if test:
        values = []
        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            tempx, tempy = (exit[0]+dx, exit[1]+dy)
            if 0 <= tempx < r and 0 <= tempy < c:
                if graph[tempx][tempy] not in [0, v+1]:
                    values.append(dfs(graph, [exit[0], exit[1]]))
        if not values:
            answer += x + 1 + 1
        else:   
            answer += max(values)
    # print(values)
    # print(answer)
    # print(graph)

print(answer)