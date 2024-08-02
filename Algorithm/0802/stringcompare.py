T = int(input())

for test_case in range(1, T+1):

    # 비교 문자 입력
    A = input()
    B = input()

    # 횟수 저장용
    cnt = 0

    # 한칸씩 이동하며 A와 B를 비교, 비교할때 같은 길이를 비교함
    for i in range(len(B)):
        if A == B[i:i+len(A)]:
            cnt += 1

    print(f'#{test_case} {cnt}')