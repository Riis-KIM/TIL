def DFS(s, v, visited=[]):
    visited.append(s)
    for item in adjL[s]:
        if item not in visited:
            DFS(item, v, visited)
    return visited

T = int(input())
for test_case in range(1, T+1):
    # V = 노드 개수, E = 연결 개수
    V, E = map(int, input().split())

# 인접 리스트
    adjL = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    visit = DFS(1, V)
    print(*visit)