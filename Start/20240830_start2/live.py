
print(0b11011110 & 0b11011)
print(bin(0b11011110 & 0b11011))

print(0x4A3 | 25)
print(bin(0x4A3), bin(25))
print(bin(0x4A3 | 25))

arr = [1,2,3,4]

# 각 자리를 쓴다/안쓴다 -> 나올 수 있는 경우의 수 = 2가지
# 각 자리마다 2가지 경우의 수 -> N 길이라면 ->2^N만큼의 경우의 수가 나올 수 있다.
print(f'부분집합의 수 : {1<<len(arr)}')

for i in range(1<<len(arr)):
    print(i, end= ' ')
print()