from collections import deque
deque_q = deque()

for i in range(100000):
    deque_q.append(i)
for _ in range(100000):
    deque_q.popleft()




# list_q = []
# for i in range(1000):
#     list_q.append(i)
# for _ in range(1000):
#     list_q.pop(0)
#
#print('end')