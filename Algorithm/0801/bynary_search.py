T = int(input())

for test_case in range(1, T+1):
    # P = 페이지 수, A = a가 찾는 페이지 위치, B = b가 찾는 페이지 위치
    P, A, B = map(int, input().split())

    count_A = 0
    count_B = 0

    find_A = False
    l = 1  # 시작 페이지
    r = P  # 마지막 페이지
    # A가 찾는 위치
    while not find_A:
        # 중간값 계산
        mid = int((l+r)/2)
        count_A +=1

        # 목표 페이지 찾으면 탈출, 아니면 count 증가 및 검색 구간 변경
        if mid == A:
            find_A = True
            break
        else:
            if mid > A:
                r = mid
            elif mid < A:
                l = mid

    find_B = False
    l = 1  # 시작 페이지
    r = P  # 마지막 페이지
    # B가 찾는 위치
    while not find_B:
        # 중간값 계산
        mid = int((l + r) / 2)
        count_B += 1
        # 목표 페이지 찾으면 탈출, 아니면 count 증가 및 검색 구간 변경
        if mid == B:
            find_B = True
            break
        else:
            if mid > B:
                r = mid
            elif mid < B:
                l = mid

    if count_A > count_B:
        print(f'#{test_case} B')

    elif count_A < count_B:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')