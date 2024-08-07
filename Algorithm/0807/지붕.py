T = int(input())

arr = []
for _ in range(T):
    arr.append(list(map(int, input().split())))

arr.sort()

# 최대 높이, 최대일때 인덱스 위치
top = 0
idx = 0
for i in range(len(arr)):
    if top < arr[i][1]:
        top = arr[i][1]
        idx = i

# 면적
box = 0
# 오른쪽 계산
t = idx
while t < len(arr):
    p = arr[t][0]
    tp = 0
    for q in range(t+1, len(arr)):
        if tp <= arr[q][1]:
            tp = arr[q][1]
            t = q
    box += (arr[t][0]+1 - p)*tp
    t+=1

# 왼쪽 계산
t = idx
while t > 0:
    p = arr[t][0]
    tp = 0
    for q in range(0, t):
        if tp <= arr[q][1]:
            tp = arr[q][1]
            t = q
    box += (p - arr[t][0]) * tp

# 꼭다리 계산
high = 0
for i in range(idx):
    if arr[i][1] > high:
        high = arr[i][1]

for i in range(idx+1, len(arr)):
    if arr[i][1] > high:
        high = arr[i][1]

box += top-high
print(box)

