# 도착 지점부터 역으로 타고 올라가서 첫번째 줄에 도착 시 해당 위치가 시작 지점임
T = 10
for test_case in range(1, T+1):
    dummy = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점 찾기
    location = 0
    for i in range(100):
        if arr[-1][i] == 2:
            location = i
            break

    T = 99
    # 시작지점까지 탐색
    while T != 0:
        # 왼쪽을 보고 갈 수 없으면 오른쪽을 확인
        # 좌 탐색, location 범위 확인
        if location - 1 >= 0 and arr[T][location - 1] == 1:
            while location - 1 >= 0 and arr[T][location - 1] == 1:
                location -= 1

        # 우 탐색, location 범위 확인
        elif location + 1 < 100 and arr[T][location + 1] == 1:
            while location + 1 < 100 and arr[T][location + 1] == 1:
                location += 1

        # 한칸 올라감
        T -= 1

    print(f'#{test_case} {location}')