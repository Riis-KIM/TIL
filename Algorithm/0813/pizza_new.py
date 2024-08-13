from collections import deque

T = int(input())

for test_case in range(1, T+1):
    # 화덕 크기, 피자 개수
    N, M = map(int, input().split())
    # 치즈
    c1 = list(map(int, input().split()))

    q = deque()

    # 큐에 치즈, 인덱스 추가
    for idx, cheese in enumerate(c1):
        q.append([cheese, idx+1])

    # 화덕
    fire = deque()
    # 화덕에 피자 넣기
    for _ in range(N):
        fire.append(q.popleft())
    # 피자 1개 남을때까지
    while len(fire) > 0:
        # 피자 확인
        pizza = fire.popleft()
        # 피자의 치즈가 다 녹았다면 새 피자 추가
        if pizza[0] // 2 == 0:
            if len(q) != 0:
                fire.append(q.popleft())
        else:   # 치즈 덜녹았으면 다시 집어넣음
            pizza[0] = pizza[0] // 2
            fire.append(pizza)

    print(f'#{test_case} {pizza[1]}')

