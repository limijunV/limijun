N, M = map(int, raw_input().split())
mat = [[int(c) for c in raw_input().strip()] for i in range(N)]
left = 0
right = sum([sum(m) for m in mat]) // 16 + 1
sums_ = [[0] * (M + 1) for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sums_[i][j] = sums_[i - 1][j] + sums_[i][j - 1] - sums_[i - 1][j - 1] + mat[i - 1][j - 1]


def sum_grid(x0, y0, x1, y1, mat):
    return sums_[x1][y1] + sums_[x0][y0] - sums_[x0][y1] - sums_[x1][y0]


def judge(mat, N, M, val):
    for r1 in range(1, N - 2):
        if sum_grid(0, 0, r1, M, mat) < 4 * val:
            continue
        for r2 in range(r1 + 1, N - 1):
            if sum_grid(r1, 0, r2, M, mat) < 4 * val:
                continue
            for r3 in range(r2 + 1, N):
                if sum_grid(r2, 0, r3, M, mat) < 4 * val:
                    continue
                if sum_grid(r3, 0, N, M, mat) < 4 * val:
                    continue
                start, count = 0, 0
                for i in range(1, M + 1):
                    if sum_grid(0, start, r1, i, mat) >= val and sum_grid(r1, start, r2, i,
                                                                          mat) >= val and sum_grid(
                            r2, start, r3, i, mat) >= val and sum_grid(r3, start, N, i, mat) >= val:
                        start, count = i, count + 1
                        if count == 4:
                            return True
    return False


while left < right:
    mid = (left + right) // 2
    state = judge(mat, N, M, mid)
    if state:
        left = mid + 1
    else:
        right = mid
print(right - 1)