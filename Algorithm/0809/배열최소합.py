# 순열을 구하고 모든 합 중에 최소값을 반환
def sumbox(i, N):
    global min_num
    # 모든 부분에 대한 순열을 구했을 경우
    if i == N:
        # 순열 합
        s= 0
        # 각 순열에 맞는 합을 구함
        for t in range(N):
            s += arr[t][result[t]]
        # 최소값 저장
        if min_num > s:
            min_num = s

    else:
        # 모든 구간에 대해서 순열 구함
        for j in range(i, N):
            result[i], result[j] = result[j], result[i]
            sumbox(i+1, N)
            result[i], result[j] = result[j], result[i]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    min_num = 100
    result = [i for i in range(N)]
    sumbox(0, N)

    print(f'{test_case} {min_num}')