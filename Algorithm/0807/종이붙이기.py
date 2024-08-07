# 재귀 사용
# def recur(N):
#     if N == 0:
#         return 1
#     elif N == 1:
#         return 1
#     else:
#         return recur(N-1) + recur(N-2)*2
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = (int(input())//10)
#
#     print(f'{test_case} {recur(N)}')


# # 메모제이션 사용
# def memo(N):
#     if arr[N] == 0:
#         arr[N] = memo(N-2)*2 + memo(N-1)
#     return arr[N]
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = (int(input())//10)
#     arr = [0] * (N+1)
#     arr[0] = 1
#     arr[1] = 1
#     print(f'#{test_case} {memo(N)}')

# DP 사용

T = int(input())

for test_case in range(1, T+1):
    N = ((int(input()))//10)

    arr = [0] * (N+1)
    arr[0] = 1
    arr[1] = 1
    for i in range(0, N-1):
        arr[i+2] = arr[i] * 2 + arr[i+1]

    print(f'#{test_case} {arr[N]}')