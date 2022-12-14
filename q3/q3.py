# import sys
# import math
#
# # Auto-generated code below aims at helping you parse
# # the standard input according to the problem statement.
#
# n = 10000
# w, h = [3, 3]
# shape = ['###', '.#.', '.#.']
# # shape = ['###', '#..', '#.#']
# # shape = ['.....', '.###.', '.#.#.', '.###.', '.....']
#
# new_shape = []
# for i in range(len(shape)):
#     for j in range(len(shape[0])):
#         if shape[i][j] == '#':
#             new_shape.append([h + i, w + j])
#             new_shape.append([h - i - 1, w - j - 1])
#             new_shape.append([h + i, w - j - 1])
#             new_shape.append([h - i - 1, w + j])
# w *= 2
# h *= 2
# shape = new_shape
# for _ in range(1, n):
#     new_shape = []
#     for idx in shape:
#         i, j = idx
#         new_shape.append([h + i, w + j])
#         new_shape.append([h - i - 1, w - j - 1])
#         new_shape.append([h + i, w - j - 1])
#         new_shape.append([h - i - 1, w + j])
#     w *= 2
#     h *= 2
#     shape = new_shape
# print('done')
# count = 0
# q = []
# while shape:
#     count += 1
#     q.append(shape.pop(0))
#     while q:
#         i, j = q.pop(0)
#         if [i+1, j] in shape:
#             shape.remove([i+1, j])
#             q.append([i+1, j])
#         if [i, j+1] in shape:
#             shape.remove([i, j+1])
#             q.append([i, j+1])
#         if [i-1, j] in shape:
#             shape.remove([i-1, j])
#             q.append([i-1, j])
#         if [i, j-1] in shape:
#             shape.remove([i, j-1])
#             q.append([i, j-1])
# print(count)



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [5, 3]
square = [[1, 1, 9, 1, 1], [1, 1, 9, 1, 1], [1, 1, 9, 1, 1]]
# for i in range(h):
#     square_h = []
#     for j in input().split():
#         square_h.append(int(j))
#     square.append(square_h)

print(square, file=sys.stderr, flush=True)

flag = True
count = 0

for n in range(h):
    for m in range(w):
        if square[n][m] > 0:
            q = [[n, m]]
        while q:
            i, j = q.pop(0)
            block = square[i][j]
            square[i][j] = 0
            if i + 1 < h and block >= square[i + 1][j] > 0 and [i + 1, j] not in q:
                q.append([i + 1, j])
            if j + 1 < w and block >= square[i][j + 1] > 0 and [i, j + 1] not in q:
                q.append([i, j + 1])
            if (i + 1 < h and block < square[i + 1][j] > 0 and j + 1 < w and block < square[i][j + 1] > 0) \
                or (i + 1 == h  and j + 1 == w) or (i + 1 == h  and j + 1 < w and block < square[i][j + 1] > 0) \
                or (i + 1 < h  and j + 1 == w and block < square[i + 1][j] > 0):
                count += 1
        # q.append()
    # and (i - 1 < 0 and block < square[i - 1][j] > 0 and j - 1 > w and block < square[i][j - 1] > 0):

# for i in range(h):
#     for j in range(w):
#         if (i + 1 < h and square[i][j] < square[i+1][j] and j + 1 < w and square[i][j] < square[i][j+1]) or (i + 1 < h and square[i][j] < square[i+1][j] and j + 1 == w) or (j + 1 < h and square[i][j] < square[i][j+1] and i + 1 == h):
#             if flag:
#                 flag = False
#             else:
#                 count += 1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(count)
