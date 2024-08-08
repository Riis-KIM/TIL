T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    count = 1
    i = 0
    summ = 0
    while i < N:
        # 만약 남은 당근이 수레 수용량 보다 작을 때
        if arr[i] <= M:
            # 전부 담을 수 있다면
            if summ + arr[i] <= M:
                # 마지막 단계일때 // 돌아오기만 하면 됨
                if i == N-1:
                    count += i+1
                    break
                # 이전 단계에서 전부 담았더니 수레가 가득 찼을때 // 비우고 다음 단계로 이동함
                elif summ + arr[i] == M:
                    arr[i] = 0
                    count += (i+1)*2
                    i += 1
                    count += 1
                # 담고 다음 단계로 넘어감
                else:
                    summ += arr[i]
                    arr[i] = 0
                    i += 1
                    count += 1
            # 전부 담을 수 없다면
            else:
                arr[i] -= (M-summ)
                summ = 0
                count += (i+1)*2
        # 만약 남은 당근이 수레 수용량 보다 클 때
        else:
            arr[i] -= (M-summ)
            summ = 0
            count += (i+1)*2

    print(f'#{test_case} {count}')