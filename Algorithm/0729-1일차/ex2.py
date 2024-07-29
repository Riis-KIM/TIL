def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

arr = [1, 5, 3, 4, 9]
print(BubbleSort(arr, 5))