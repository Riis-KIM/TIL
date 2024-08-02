# 해당 문제는 이동 방향이 무조건 오른쪽, 아래, 왼쪽, 위쪽 시계방향으로 움직이고
# 각 방향으로 움직이는 횟수는 [N, N-1, N-1, N-2, N-2.....]로 움직인다
# 아래 함수는 움직이는 횟수를 저장하는 배열을 만드는 함수
def pattern(N):
    arr = []
    for i in range(N, 0, -1):
        arr.append(i)
        if i - 1 > 0:
            arr.append(i - 1)
    return arr


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    # 델타 사용, 오른쪽, 아래, 왼쪽, 위쪽
    location = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 움직이는 횟수 저장
    move = pattern(N)

    # 이동 횟수
    count = 0
    # 시작 위치
    l = 0
    c = -1
    # 델타 인덱스 번호, 현재 움직이는 방향 저장용
    loc_idx = 0
    # N*N보다 작을 때
    while count < N**2:
        # 정해진 이동 횟수만큼 반복
        for item in move:
            for i in range(item):
                # 이동 횟수 증가
                count += 1
                # 위치 변환
                l += location[loc_idx][0]
                c += location[loc_idx][1]
                arr[l][c] = count
            # idx가 3이다 ==> 다음은 다시 오른쪽으로 가야하기 때문에
            if loc_idx == 3:
                loc_idx = 0
            else:
                loc_idx += 1

    print(f'#{test_case}')
    for tem in arr:
        print(*tem)