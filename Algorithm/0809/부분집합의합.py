def f1(i, V):           #V개의 집합에서 i원소의 포함여부 결정
    if i ==V:               #모든 원소에 의해 결정하면
        print(b)
    else:
        b[i] = 1        # a[i]가 부분집합에 포함되는 경우
        f1(i+1, V)
        b[i] = 0
        f1(i+1, V)

def f2(i, V, K):
    global cnt
    if i == V:               #모든 원소에 의해 결정하면
        s = 0               # 부분집합의 합 저장
        for j in range(V):
            if b[j]:        #a[j]가 포함되면
                s += a[j]
        # print(s)
        if s == K:
            cnt += 1
    else:
        b[i] = 1        # a[i]가 부분집합에 포함되는 경우
        f2(i+1, V, K)
        b[i] = 0
        f2(i+1, V, K)


def f3(i, V, N, K): # i고려할 원소, V 원소 수, N 부분집합 원소수, K 찾는 합
    global cnt
    if i ==V:               #모든 원소에 의해 결정하면
        s = 0               # 부분집합의 합 저장
        c = 0               # 부분집합 원소 수
        for j in range(V):
            if b[j]:        #a[j]가 포함되면
                s += a[j]
                c += 1
        # print(s)
        if c==N and s == K:          # 부분집합의 합이 K인 경우
            cnt += 1
    else:
        b[i] = 1        # a[i]가 부분집합에 포함되는 경우
        f3(i+1, V, N ,K)
        b[i] = 0
        f3(i+1, V, N, K)


def f4(i, V, N, K, s):  # i고려할 원소, V 원소 수, N 부분집합 원소수, K 찾는 합,
                           # s 이전까지 포함된 부분집합 원소 합
    global cnt
    global fcnt
    fcnt += 1
    if i == V:          # 모든 원소 고려
        if s == K:      # 부분집합의 합이 K인 경우
            cnt += 1
    elif s>K:           # 포함된 원소의 합이 이미 목표를 초과한 경우
        return          # 포함된 원소 재 선택
    else:
        b[i] = 1
        f4(i+1, V,N,K,s+a[i])       # s+a[i] a[i]를 포함한 경우 원소의 합
        b[i] = 0
        f4(i+1,V,N,K,s)             # a[i]가 포함되지 않은 경우 선택된 원소의 합


def f5(i, V, N, K, c, s):  # i고려할 원소, V 원소 수, N 부분집합 원소수, K 찾는 합,
# s 이전까지 포함된 부분집합 원소 합 c 선택한 원소 개수

    global cnt
    global fcnt
    fcnt += 1
    if c == N and s == K: # 부분집합의 합이 K인 경우
        cnt += 1
    elif i == V:        # 모든 원소 고려
        return
    elif c > N or s > K:    # 포함된 원소의 합이 이미 목표를 초과했을 경우
        return              # 포함된 원소 재 선택
    else:
        b[i] = 1
        f4(i + 1, V, N, K, s + a[i])  # s+a[i] a[i]를 포함한 경우 원소의 합
        b[i] = 0
        f4(i + 1, V, N, K, s)  # a[i]가 포함되지 않은 경우 선택된 원소의 합

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    a = [i for i in range(1, N+1)]
    b = [0]*N
    # 재귀로 모든 부분집합 만들기
    # f1(0, 12)       # 총 12개의 원소, a[0]부터 포함여부 결정하기
    # # 부분집합의 합이 K인 경우의 수 찾기
    # cnt = 0
    # f3(0, 12, N, K)
    # # -----------------------------------
    # 원소의 개수가 N개이면서, 합이 K인 부분집합의 수 cnt 찾기
    # cnt = 0
    # f3(0, 12, N, K)
    # print(cnt)

    cnt = 0
    fcnt = 0
    f4(0, 12, N, K, 0, 0)
    print(cnt, fcnt)