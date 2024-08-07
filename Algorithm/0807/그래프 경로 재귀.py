def DFS(s, v):
    v.append(s)
    for item in arr[s]:
        if item not in v:
            DFS(item, v)
    return v

def DFS2(i, G):
    if i == G:
        return 1
    else:
        visited[i] = 1
        for w in arr[i]:
            if visited[w] == 0:
                if DFS2(w, G):
                    return 1
        return 0

# 1번의 경우
# T = int(input())
# for test_case in range(1, T+1):
#     # V = 노드 개수, E = 연결 개수
#     V, E = map(int, input().split())
#
#     # V의 개수만큼 빈 배열 생성
#     arr = [[] for _ in range(V + 1)]
#
#     for _ in range(E):
#         # s1 = 시작 노드 s2 = 끝 노드
#         s1, s2 = map(int, input().split())
#         # 한 방향으로만 이동 가능하기 때문
#         arr[s1].append(s2)
#
#     # S = 시작노드 G = 끝 노드
#     S, G = map(int, input().split())
#
#     visited = []
#     visit = DFS(S, visited)
#     flag = 0
#     if G in visit:
#         flag = 1
#     print(f'#{test_case} {flag}')

T = int(input())
for test_case in range(1, T+1):
    # V = 노드 개수, E = 연결 개수
    V, E = map(int, input().split())

    # V의 개수만큼 빈 배열 생성
    arr = [[] for _ in range(V + 1)]

    for _ in range(E):
        # s1 = 시작 노드 s2 = 끝 노드
        s1, s2 = map(int, input().split())
        # 한 방향으로만 이동 가능하기 때문
        arr[s1].append(s2)

    # S = 시작노드 G = 끝 노드
    S, G = map(int, input().split())

    visited = [0]*(V+1)
    visit = DFS2(S, G)

    print(f'#{test_case} {visit}')