SIZE = 50
stack = [0] * SIZE
top = -1

top += 1
stack[top] = 1
top += 1
stack[top] = 2
top += 1
stack[top] = 3

top -=1
print(stack[top+1])
print(stack[top])
top -= 1
print(stack[top])
top-=1