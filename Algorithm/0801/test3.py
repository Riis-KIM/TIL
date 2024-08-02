T = 10

for test_case in range(1, T + 1):
    dummy = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    for start in range(100):
        if arr[0][start] == 1:
            i, j = 0, start
            while i < 99:
                # 좌측 확인
                if 0 <= j - 1 and arr[i][j - 1] != 0:
                    while 0 <= j - 1 and arr[i][j - 1] != 0:
                        j -= 1
                # 우측 확인
                elif j + 1 < 100 and arr[i][j + 1] != 0:
                    while j + 1 < 100 and arr[i][j + 1] != 0:
                        j += 1

                if i + 1 < 100 and arr[i + 1][j] != 0:
                    i += 1

        if arr[i][j] == 2:
            print(start)
            break