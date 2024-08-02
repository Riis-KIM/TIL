
T = int(input())

for test_case in range(1, T+1):

    # A, B를 리스트로 받아옴
    A = list(input())
    B = list(input())

    # 최대값 저장용
    max_count = 0

    # A의 문자와 B의 문자를 비교해서 같을 경우 횟수 증가
    for item in A:
        cnt = 0
        for tem in B:
            if item == tem:
                cnt += 1
        # 최대값 저장
        if max_count < cnt:
            max_count = cnt

    print(f'#{test_case} {max_count}')