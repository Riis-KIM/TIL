T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    # 미로 저장용, N*N 미로임
    arr = []
    for _ in range(N):
        arr.append([int(s) for s in input()])

    # 델타 사용 // 동 남 서 북
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # 시작 위치 찾음
    start_idx = [0,0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_idx = [i, j]

    # 시작 인덱스
    i = start_idx[0]
    j = start_idx[1]
    # 방문 한 장소
    stack = []
    visited = [[0] * N for _ in range(N)]
    # 찾았는지 확인용
    flag = 0
    while True:
        # 방문표시
        visited[i][j] = 1
        # 도착지점 도착시
        if arr[i][j] == 3:
            flag = 1
            break
        # 모든 방향에 대해서
        for k in delta:
            ni, nj = i + k[0], j + k[1]
            # 범위 밖을 벗어나지 않고 벽(1)이 아니고 방문한 적 없을 경우
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                # 이동 전 위치 저장 후 이동
                stack.append([i, j])
                i, j = ni, nj
                break
        # 모든 방향을 둘러봐도 더이상 갈 수 없을때
        else:
            # 이전 위치로 이동
            if stack:
                stacked_idx = stack.pop()
                i = stacked_idx[0]
                j = stacked_idx[1]
            # 모든 위치를 확인했는데도 목표에 도달하지 못했을 경우
            else:
                flag = 0
                break
    print(f'#{test_case} {flag}')

