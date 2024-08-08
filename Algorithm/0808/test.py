T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    ans_max = 0
    for i in range(n):
        for j in range(m):
            current_sum = arr[i][j]
            length = arr[i][j]
            for k in range(4):
                ni, nj = i, j
                for _ in range(length):
                    ni += di[k]
                    nj += dj[k]
                    if 0 <= ni < n and 0 <= nj < m:
                        current_sum += arr[ni][nj]
            if ans_max < current_sum:
                ans_max = current_sum

    print(f'#{tc} {ans_max}')