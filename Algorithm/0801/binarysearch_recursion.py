
# l = 시작, r = 끝 g = 목표, c = 카운트 수
def binary(l, r, g, c):
    c += 1
    middle = (l+r)//2

    if middle < g:
        return binary(middle, r, g, c)
    elif middle > g:
        return binary(l, middle, g, c)
    else:
        return c

T = int(input())

for test_case in range(1, T+1):
    # P = 페이지 수, A = a가 찾는 페이지 위치, B = b가 찾는 페이지 위치
    P, A, B = map(int, input().split())

    # 각각의 탐색 횟수 기록
    count_A = binary(1, P, A, 0)
    count_B = binary(1, P, B, 0)

    # 탐색 횟수 비교
    if count_A > count_B:
        print(f'#{test_case} B')

    elif count_A < count_B:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')
