T = int(input())
for test_case in range(1, T+1):
    dummy = input()
    arr = list(map(int, input().split()))

    # 점수 저장용
    score_arr = [0] * 101

    # 점수 개수 저장
    for item in arr:
        score_arr[item] += 1

    # 점수 개수 가장 큰 점수 저장
    max_idx = 0
    for i in range(len(score_arr)-1, -1, -1):
        if score_arr[i] > score_arr[max_idx]:
            max_idx = i

    print(f'#{test_case} {max_idx}')