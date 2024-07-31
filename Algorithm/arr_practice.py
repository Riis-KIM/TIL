arr =[[1,2,3], [4,5,6]]
arr = [[0]*3]*2
print(arr)

## 5x5 2차원 배열에 25개 숫자 저장하고 대각선 원소 구함

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

di = [0,1,0,-1]
dj = [1, 0, -1, 0]

total = 0

for i in range(N):
    for j in range(N):
        num_sum = 0
        # i , j 원소의 4방향으로(3시방향부터 시계방향으로)
        for k in range(4):
            ni = i+ di[k]
            nj = j+ dj[k]
            if 0<= ni< N and 0<= nj< N:
                num_sum += abs(arr[ni][nj] - arr[i][j])
        
        total += num_sum
print(total)

bit = [0, 0, 0, 0] # 1 또는 0

for i in range(2):
    bit[0] = i                  #1번 원소
    for j in range(2):
        bit[1] = j              #2번 원소
        for k in range(2):      #3번 원소
            bit[2] = k
            for l in range(2):  #4번 원소
                bit[3] = l
                print(bit)