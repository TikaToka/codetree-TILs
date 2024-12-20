n = int(input())

edges = [[] for _ in range(n)]

temp = list(map(int, input().split()))

for idx, i in enumerate(temp):
    if i == -1:
        continue
    else:
        edges[idx].append(i)
        edges[i].append(idx)
    
d = int(input())

visited = []
p = temp[d]
def traverse(x):
    visited.append(x)
    for y in edges[x]:
        if y == p:
            continue
        if y not in visited:
            traverse(y)

traverse(d)


for i in visited:
    temp[i] = -1

answer = 0

for i in range(n):
    if i not in temp and i not in visited:
        answer +=1
# print(visited)
# print(temp)
print(answer)
