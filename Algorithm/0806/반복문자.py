T = int(input())
for test_case in range(1, T+1):
    str1 = input()

    # arr = stack, idx = 문자열 위치 i = 스택 위치
    arr = []
    idx = 0
    i = 0

    # 모든 문자열을 순회하며 스택에 추가
    while idx < len(str1):
        arr.append(str1[idx])
        idx += 1
        i += 1
        # 겹치는 문자 발견 시 삭제
        if i > 1 and arr[i-1] == arr[i-2]:
            arr.pop()
            arr.pop()
            i -= 2

    print(f'#{test_case} {len(arr)}')