def dfs2(i, j, N):
    visited[i][j] = 1
    if maze[i][j] == 3:
        return 1
    else:
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i +di, j +dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                if dfs2(ni,nj,N):
                    return 1
        return 0

def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

def dfs(i, j, N):
    stack = []          #스택 생성, visited는 외부에서 생성(내부에서 선언해도 무관)
    visited[i][j] = 1   # 시작점 방문표시
    while True:         # 인접칸으로 갈 수 있으면 경로를 저장하고 이동하는 방식
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:       # i, j에 인접 ni, nj중에 이동가능한 곳이 있는지 확인
            ni, nj = i +di, j +dj
            # 벽으로 둘러지지 않은 미로, 벽이 아닌 칸
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                visited[ni][nj] = 1        # v에 인접하고 미방문인 w가 있으면
                stack.append([i,j])         # 스택에 경로 저장
                i, j = ni, nj           # w로 이동
                break               # for di, dj, 이동 완료
        else:                       # 이동 가능한 칸이 없으면
            if stack:               # 지나온 칸이 있으면
                i, j = stack.pop()      # 그 칸에서 다른 방향을 탐색
            else:
                return 0

    return -1       # 비정상 탐색 종료


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발 위치 찾기
    sti, stj = fstart(N)
    visited = [[0]*N for _ in range(N)]
    result = dfs(sti, stj, N)