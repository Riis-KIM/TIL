

for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    total = 0
    # 해당 건물 기준 왼쪽 -2, -1 보다 크고 오른쪽 1, 2보다 클 경우를 찾아야함
    for i in range(2, N-2):
        height = 0
        dummy_list = []
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i+1] < arr[i] and arr[i+2] < arr[i]:
            dummy_list.extend(arr[i-2:i+3])
            del dummy_list[2]
            high = 0
            for t in dummy_list:
                if t > high:
                    high = t
            total += arr[i]-high

    print(f'#{test_case} {total}')


# for test_case in range(1, 11):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     total = 0
#     # 해당 건물 기준 왼쪽 -2, -1 보다 크고 오른쪽 1, 2보다 클 경우를 찾아야함
#     for i in range(2, N-2):
#         height = 0
#         dummy_list = []
#         if arr[i-2] < arr[i]:
#             if arr[i-1] < arr[i]:
#                 if arr[i+1] < arr[i]:
#                     if arr[i+2] < arr[i]:
#                         dummy_list.append(arr[i - 2])
#                         dummy_list.append(arr[i - 1])
#                         dummy_list.append(arr[i + 1])
#                         dummy_list.append(arr[i + 2])
#                         dummy_list.sort()
#                         total += arr[i]-dummy_list[-1]
#
#     print(f'#{test_case} {total}')
