
data = [1 ,3 ,4 ,2, 5, 6, 9]
count = [0] * max(data)

temp = [0] * len(data)

# count에 개수 지정
for item in data:
    count[item-1] += 1

# count에 위치 지정
for i in range(len(count)-1):
    count[i+1] += count[i]

# append 사용하면 되는거 아닌가..?
# for j in range(len(count)):
#     for t in range(count[j]):
#         temp.append(j+1)


# print(*temp)

for i in range(len(temp)-1, -1, -1):
    count[data[i]-1] -=1
    temp[count[data[i]-1]] = data[i]

print(*temp)