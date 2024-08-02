d = 10
for test_case in range(1, d+1):
    dummy = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    # 모든 시작 지점에 대해서
    for i in range(100):
        if arr[0][i] == 1:
            # 현재 위치
            T = 1
            location = i
            # 바닥에 도착할 때 까지 반복
            while T < 99:
                # 좌 탐색, location 범위 확인
                if location - 1 >= 0 and arr[T][location - 1] == 1:
                    while location - 1 >= 0 and arr[T][location - 1] == 1:
                        location -= 1

                # 우 탐색, location 범위 확인
                elif location + 1 < 100 and arr[T][location + 1] == 1:
                    while location + 1 < 100 and arr[T][location + 1] == 1:
                        location += 1
                # 한칸 아래로
                T += 1
            # 만약 현재 도착 지점이 찾던 도착 지점일 경우
            if arr[T][location] == 2:
                print(f'#{test_case} {i}')
                break
