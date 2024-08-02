def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


def bino(n, k):
    return int(factorial(n) / (factorial(k)*factorial(n-k)))


N, K = map(int, input().split())

arr = [1,1]
for i in range(N, N-K, -1):
    arr[0] *=i
for j in range(K, 0, -1):
    arr[1] *=j
print(int(arr[0]/arr[1]))