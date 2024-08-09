def f(i, N):        # 크기가 N인 순열을 저장한 p배열에서 p[i를 정하는 함수
    global min_v
    if i == N:      #
        s = 0
        for j in range(N):
            s += arr[j][p[j]]
        if min_v > s:
            min_v = s
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)   # i+1자리 결정
            p[i], p[j] = p[j], p[i]


def f2(i, N, s):        # 크기가 N인 순열을 저장한 p배열에서 p[i]를 정하는 함수
                        # s : i-1행까지 선택된 원소의 합
    global min_v
    global fcnt
    fcnt +=1
    if i == N:      #
        if min_v > s:
            min_v = s
    elif min_v <= s:
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f2(i+1, N, s+arr[i][p[i]])   # i+1자리 결정
            p[i], p[j] = p[j], p[i]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    # 각 행에서 1개의 원소 고르기, 단 한열에서 한 개만 선택가능
    # 선택한 원소 합의 최솟값
    min_v = 10000 # 3<=N<=10, A,i,j <=9
    p = [i for i in range(N)]         # p[i] : i행에서 선택한 열 번호
    f(0, N)