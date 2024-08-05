T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # 위치 저장
    counts = [0] * 5001
    for line in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            counts[i] += 1

    P = int(input())
    print(f'#{test_case}', end = ' ')
    # 요구하는 정류소 번호에 겹치는 버스노선 출력
    for _ in range(P):
        c = int(input())
        print(counts[c], end = ' ')
    print()