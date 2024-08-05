#
# lps[0] = -1
#
# for i in range(1, M):
#     lps[i] = j
#     while i<N:
#         if pat[j] == txt[i]
#             i+=1
#             j+=1
#
#         if j == M:
#             j = lps[j-1]
#
#         elif i < N and pat[j] != txt[i]

def f(t, p):
    N = len(t)
    M = len(p)

    for i in range(N-M+1):
        for j in range(M):
            if t[i+j]!=p[j]:
                break
        else:
            return i
    return -1
