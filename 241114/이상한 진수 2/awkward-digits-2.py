def binary2decimal(n):
    n = reversed(n)
    output = 0
    cnt = 0
    for i in n:
        output += int(i) * (2 ** cnt)
        cnt += 1
    return output
n = list(input())

changed = False
for i in range(len(n)):
    if n[i] == '0':
        n[i] = '1'
        changed = True
        break

if not changed:
    if n[-1] == '1':
        n[-1] = '0'
    elif n[-1] == '0':
        n[-1] = '1'

answer = binary2decimal(n)
print(answer)