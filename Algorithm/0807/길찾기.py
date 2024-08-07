
# DFS 이용, s = 시작점
def DFS(s):
    visited[s] = 1
    v = s
    stack = []
    while True:
        # 이동 가능한 경로 중
        for item in adj[v]:
            # 방문한 적 없으면 현재 위치 stack에 추가하고 이동 후 방문 표시
            if visited[item] == 0:
                stack.append(v)
                v = item
                visited[item] = 1
                break
        else:
            # 현재 위치에서 전부 방문했다면 이전 분기점으로 돌아감
            if stack:
                v = stack.pop()
            else:
                break

# 테스트 케이스 10개
T = 10
for test_case in range(1, T+1):
    A, N = map(int, input().split())

    # 인접 리스트로 변환
    arr = list(map(int, input().split()))
    adj = [[] for _ in range(100)]
    for i in range(N):
        s1 = arr[i*2]
        s2 = arr[i*2+1]
        adj[s1].append(s2)
    # 이동 표시
    visited = [0] * 100
    # 시작점은 0이고, 도착점은 99
    DFS(0)
    print(f'#{test_case} {visited[99]}')
