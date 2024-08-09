# 가위바위보 승자 구하는 함수
def rps(a,b):
    # 같은거 냈을 때
    if arr[a] == arr[b]:
        return a
    # b가 이기는 경우
    elif (arr[a] == 1 and arr[b] == 2) or (arr[a] == 2 and arr[b] == 3) or (arr[a] == 3 and arr[b] == 1):
        return b
    # a가 이기는 경우
    else:
        return a


# 대진표 편성 후 최종 승자를 구하는 함수
def win(i, j):    #i~j 번 승자 찾기
    if i==j:
        return i
    else:
        mid = (i+j)//2
        left = win(i, mid)       #왼쪽 그룹
        right = win(mid+1, j)    #오른쪽 그룹
        return rps(left, right)


T = int(input())


for test_case in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    # 인덱스 번호 입력
    ans = win(0, N-1)+1

    print(f'#{test_case} {ans}')