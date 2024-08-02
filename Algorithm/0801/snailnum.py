T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    # 델타 사용, 오, 밑, 왼, 위
    location = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # 시작 위치는 1부터
    arr[0][0] = 1
    #  count = 다음 점수, i, j = 시작 위치
    count = 2
    i = 0
    j = 0

    # count 가 NxN 이하일때
    while count <= N**2:
        # 델타 이용해 모든 방향에 대해 이동함
        for item in location:
            # 한쪽 방향으로 나아갈 수 있을만큼 나아감, 범위 내인지 확인
            while 0 <= i+item[0] < N and 0 <= j+item[1] < N:
                # 0이 아님 => 이미 지나갔던 장소
                if arr[i+item[0]][j+item[1]] != 0:
                    break
                # 움직인 만큼 위치 변경, 칸에 숫자 채움
                i += item[0]
                j += item[1]
                arr[i][j] = count
                count += 1
    print(f'#{test_case}')
    for tem in arr:
        print(*tem)