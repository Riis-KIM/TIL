T = int(input())

for test_case in range(1,T+1):

    str1 = input()
    str2 = input()

    ans = 0
    for i in range(len(str2)-len(str1)+1):
        if str1 == str2[i:i+len(str1)]:
           ans = 1

    print(f'#{test_case} {ans}')