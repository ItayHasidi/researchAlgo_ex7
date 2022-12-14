import sys
import math
n = int(input())
w, h = [int(i) for i in input().split()]
shape = []
for i in range(h):
    row = input()
    shape.append(row)
for _ in range(n):
    new_shape = []
    last_shape = []
    for i in range(len(shape)):
        new_shape.append(shape[len(shape) - 1 - i])
    for i in range(len(shape)):
        new_shape.append(shape[i])
    for i in range(len(new_shape)):
        curr_line = []
        for j in range(len(new_shape[i])):
            curr_line.append(new_shape[i][len(new_shape[i]) - 1 - j])
        for j in range(len(new_shape[i])):
            curr_line.append(new_shape[i][j])
        last_shape.append(curr_line)
    shape = last_shape
count = 0
q = []
for n in range(len(shape)):
    for m in range(len(shape[n])):
        if shape[n][m] == '#':
            count += 1
            q.append([n, m])
            while q:
                i, j = q.pop(0)
                curr_pix = shape[i][j]
                if curr_pix == '#':
                    shape[i][j] = '-'
                    if i + 1 < len(shape) and j < len(shape[0]) and [i + 1, j] not in q and shape[i + 1][j] == '#':
                        q.append([i + 1, j])
                    if j + 1 < len(shape[0]) and i < len(shape) and [i, j + 1] not in q and shape[i][j + 1] == '#':
                        q.append([i, j + 1])
                    if i - 1 >= 0 and j < len(shape[0]) and [i - 1, j] not in q and shape[i - 1][j] == '#':
                        q.append([i - 1, j])
                    if j - 1 >= 0 and i < len(shape) and [i, j - 1] not in q and shape[i][j - 1] == '#':
                        q.append([i, j - 1])
print(count)
