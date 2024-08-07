T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    # 삼각형 시작
    arr = [[1]]
    for i in range(1, N):
        # 복사용 추가 배열
        dummy = [1]
        # (-1, -1) + (-1, 0) 하기 위함
        for j in range(1, i):
            dummy.append(arr[i-1][j-1] + arr[i-1][j])
        # 마지막에 1 추가
        dummy.append(1)
        # 추가 배열 덧붙임
        arr.append(dummy)
    # 결과 출력
    print(f'#{test_case}')
    for item in arr:
        print(*item)
