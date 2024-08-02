num = int(input())

arr = list(map(int, input().split()))

top = max(arr)

for i in range(len(arr)):
    arr[i] = (arr[i] / top) * 100

print(sum(arr)/len(arr))
