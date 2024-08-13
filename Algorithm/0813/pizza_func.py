def last_pizza(N, M, c1):
    # 화덕, 피자 인덱스 저장용 배열
    queue = [0] * N
    pizza_idx = [0] * N
    # 현재 몇번째 피자인지, 현재 화덕 내 어떤 피자가 입구쪽인지
    i = 0
    queue_idx = 0
    while True:
        # 치즈 양 절반으로 줄임
        queue[queue_idx] = queue[queue_idx] // 2
        # 남아있는 피자가 있고 비어있거나 치즈가 전부 녹았을 경우
        if queue[queue_idx] == 0 and i < M:
            queue[queue_idx] = c1[i]
            pizza_idx[queue_idx] = i + 1
            i += 1
        # 다음 피자로
        queue_idx = (queue_idx + 1) % N

        # 화덕 내 남아있는 피자가 1개뿐일때 남은 피자 번호 반환
        if i == M and len([x for x in queue if x != 0]) == 1:
            for j in range(N):
                if queue[j] != 0:
                    return pizza_idx[j]


T = int(input())

for test_case in range(1, T+1):
    # 화덕 크기, 피자 개수
    N, M = map(int, input().split())
    # 치즈
    c1 = list(map(int, input().split()))

    print(f'#{test_case} {last_pizza(N, M, c1)}')