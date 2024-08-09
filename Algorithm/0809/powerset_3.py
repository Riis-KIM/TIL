def f(i,k,s,t):     # i 원소, k 집합의 크기, s i-1까지 고려된 합, t 목표
    global cnt
    global fcnt
    fcnt += 1
    if s >t: # 모든 요소 고려
        return
    elif s==t:
        cnt +=1
        return
    elif i == k:
        return

    if s==t:
        cnt += 1
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t) # A[i]포함
        bit[i] = 0
        f(i+1, k, s,t) # A[i] 미포함


def f(i, k, s, t):  # i 원소, k 집합의 크기, s i-1까지 고려된 합, t 목표
    global cnt

    if s >t:                # 모든 요소 고려
        return
    elif s == t:
        cnt += 1
        return
    else:
        bit[i] = 1
        f(i + 1, k, s + A[i], t)  # A[i]포함
        bit[i] = 0
        f(i + 1, k, s, t)  # A[i] 미포함


A = [1, 2, 3,4,5,6,7,8,9,10]
N = 10

key = 55
cnt = 0         # 합이 key와 같은 부분집합의 수
bit = [0]*N
fcnt = 0
f(0,N,0,key)

print(cnt, fcnt)