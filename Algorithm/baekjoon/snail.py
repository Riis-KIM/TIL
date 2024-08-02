
# A = 올라감 B = 내려감 V = 목표높이
A, B, V = map(int, input().split())

if (V-B) % (A-B) == 0:
    print((V-B)//(A-B))
else:
    print((V-B)//(A-B)+1)