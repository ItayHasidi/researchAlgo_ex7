import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = 2
w, h = [3, 3]
shape = ['###', '.#.', '.#.']
# shape = ['###', '#..', '#.#']
# for i in range(h):
#     row = input()
#     shape.append(row)
# print(shape)
# print(n, shape, file=sys.stderr, flush=True)

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
    # print(len(last_shape))
    # shape = []
    # new_shape = []
    shape = last_shape  # .copy()
    # last_shape = []

print("len: ", len(shape), file=sys.stderr, flush=True)

# print(last_shape)

count = 0
q = []
# print("len: ",len(last_shape), file=sys.stderr, flush=True)

for n in range(len(shape)):
    for m in range(len(shape[n])):
        if shape[n][m] == '#':
            count += 1
            # print(n, m, file=sys.stderr, flush=True)
            q.append([n, m])
            while q:
                i, j = q.pop(0)
                curr_pix = shape[i][j]
                if curr_pix == '#':
                    # count += 1
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
