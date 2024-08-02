def GCD(x,y):
    while(y):
        x, y = y, x%y
    return x

def LCM(x,y):
    return (x*y) // GCD(x,y)

A, B = map(int, input().split())

print(GCD(A, B))
print(LCM(A, B))

