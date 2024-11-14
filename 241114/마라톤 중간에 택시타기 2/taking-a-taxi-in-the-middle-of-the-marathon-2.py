def mDist(n1, n2):
    x1, y1 = n1
    x2, y2 = n2
    return abs(x1-x2) + abs(y1-y2)

N = int(input())
ckpt = []
for i in range(N):
    x, y = map(int, input().split())
    ckpt.append((x, y))

answer = 99999999999999999999

for i in range(1, N-1):
    temp = ckpt[:]
    temp.pop(i)
    cand = 0
    for j in range(len(temp)-1):
        cand += mDist(temp[j], temp[j+1])
    answer = min(answer, cand)

print(answer)