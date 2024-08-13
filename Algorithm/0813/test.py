T = int(input())
for tc in range(1, T + 1):
    test = list(input().split())

    blue = [1, 0]  # 위치, 마지막 작업 시간
    orange = [1, 0]

    for i in range(1, int(test[0]) * 2 + 1, 2):  # i = 1, 3, 5, ....
        if test[i] == 'B':  # 로봇 결정 ,test[i+1] 스위치번호
            dist = abs(blue[0] - int(test[i + 1]))  # 거리
            blue[1] = max(blue[1] + dist + 1, orange[1] + 1)  # 마지막 작업 시간
            blue[0] = int(test[i + 1])  # 마지막 작업 위치
        else:  # O
            dist = abs(orange[0] - int(test[i + 1]))  # 이동거리
            orange[1] = max(orange[1] + dist + 1, blue[1] + 1)  #
            orange[0] = int(test[i + 1])
    print(f'#{tc} {max(blue[1], orange[1])}')