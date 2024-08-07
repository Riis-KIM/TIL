def DFS(s, g, N):
    # 방문했는지 기록하기 위함
    visited = [0]*(N+1)
    # 스택 생성
    stack = []
    # 시작 위치 방문 기록
    visited[s] = 1
    v = s
    # 목표 방문했는지 기록용
    flag = 0
    while True:
        # 방문 가능한 위치 중에서
        for w in arr[v]:
            # 아직 방문하지 않은 곳에 대해
            if visited[w] == 0:
                stack.append(v)
                v = w
                visited[w] = 1
                # 새로운 곳이 목표라면
                if v == g:
                    flag = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return flag

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())

    # V의 개수만큼 빈 배열 생성
    arr = [[] for _ in range(V+1)]

    for _ in range(E):
        # s1 = 시작 노드 s2 = 끝 노드
        s1, s2 = map(int, input().split())
        # 한 방향으로만 이동 가능하기 때문
        arr[s1].append(s2)

    # S = 시작노드 G = 끝 노드
    S, G = map(int, input().split())

    print(f'#{test_case} {DFS(S, G, V)}')