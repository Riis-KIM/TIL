T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    idx = 1
    count = 1
    max_count = 1
    while idx < N:
        if arr[idx] > arr[idx-1]:
            count+=1
        else:
            if count > max_count:
                max_count = count
            count = 1
        idx +=1

    if count > max_count:
        max_count = count
    print(f'#{test_case} {max_count}')
