T = int(input())

for test_case in range(1, T+1):
    A, B = map(str, input().split())
    count = 0
    i = 0

    while i <= len(A) - len(B):
        if A[i:i+len(B)] == B:
            count += 1
            i += len(B)
        else:
            i += 1

    ans = len(A) - count*(len(B)-1)
    print(f'#{test_case} {ans}')
