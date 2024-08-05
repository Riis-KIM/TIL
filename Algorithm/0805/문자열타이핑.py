T = int(input())

for test_case in range(1,T+1):

    A, B = map(str, input().split())

    # 횟수 저장용
    count = 0
    i = 0

    # A를 반복하며 B가 있는지 확인
    while i < len(A):
        count += 1
        if A[i:i+len(B)] == B:
            i += len(B)
            continue
        i+=1

    print(f'#{test_case} {count}')