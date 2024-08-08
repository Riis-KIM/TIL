T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))
    arr.sort()

    # arr1 = 소, arr2 = 중, arr3 = 대
    arr1 = []
    arr2 = []
    arr3 = []

    